import pyttsx3 as tts
import speech_recognition as sr
import mysql.connector as mc
from text2digits import text2digits as ttd
from datetime import date, time, datetime


def message(msg):
    engine = tts.init()
    engine.setProperty('rate', 150)
    engine.say(msg)
    engine.runAndWait()


class StartVotingSystem:
    def __init__(self, today):
        self.startTime = time(hour=8, minute=0, second=0)
        self.startDay = today
        self.endTime = time(hour=17, minute=0, second=0)
        if date.today() != self.startDay:
            message("Sorry you cannot access this system as the day for voting is not today")
        else:
            currentTime = datetime.now().time()
            if currentTime < self.startTime:
                message("System is not yet initiated, comeback when it's 8 AM")
            else:
                # included for the program to run until a specified time
                while currentTime < self.endTime:
                    self.initialize_system = VotingSystem()
                    currentTime = datetime.now().time()
                    # included for testing purposes when the system goes into use, will be removed
                    break
                self.initialize_system.declare_winner()


class VotingSystem:

    def __init__(self):
        # connecting to the database and initializing the system
        serverName = "localhost"
        dbPass = ""
        dbUsername = "root"
        database = "voting_system"
        self.conn = mc.connect(host=serverName, password=dbPass, user=dbUsername, database=database)
        self.cursor = self.conn.cursor()
        # sql to get the number of candidates to take part in the election
        sql = "SELECT COUNT(Identifier) FROM candidates"
        self.cursor.execute(sql)
        number = self.cursor.fetchall()
        self.candidatesNumber = number[0][0]
        # candidates would be a variable to hold all the candidates in the election
        self.candidates = []
        for index in range(1,  self.candidatesNumber + 1):
            self.candidates.append({f"Candidate {index}": "none"})
        self.fetch_candidate(c_ids=self.candidatesNumber + 1)
        self.introductory_message()

    def fetch_candidate(self, c_ids):
        # results variable holds the details of the candidates in the database
        # needed for the system to be able to mention the current candidates for the voter to make a decision
        # as to who to vote for
        results = []
        for ids in range(1, c_ids + 1):
            stmt = "SELECT Identifier, Name, Party FROM candidates WHERE Identifier = %s"
            self.cursor.execute(stmt, (ids,))
            results.append(self.cursor.fetchall())
        j = 1
        for index in range(0, len(results) - 1):
            self.candidates[index][f"Candidate {j}"] = {"Number": results[index][0][0], "Name": results[index][0][1],
                                                        "Party": results[index][0][2]}
            j += 1

    def introductory_message(self):
        message("Welcome from the voting system.")
        message("The details of the various candidates would be mentioned,")
        message("To cast a vote, you say the number corresponding to the candidate you wish to vote for...")
        message("Your vote will then be recorded...")
        message("Note: you can only attempt to vote once...")
        message("Please listen attentively as the candidates are announced,")
        self.announce_candidates()

    def announce_candidates(self):
        engine = tts.init()
        engine.setProperty("rate", 150)
        i = 1
        for candidate in self.candidates:
            engine.say(f"Candidate Number: {candidate[f'Candidate {i}']['Number']}")
            engine.say(f"Candidate Name: {candidate[f'Candidate {i}']['Name']}")
            engine.say(f"Candidate Party: {candidate[f'Candidate {i}']['Party']}")
            if candidate[f'Candidate {i}']['Number'] != self.candidatesNumber:
                engine.say("Next...")
            engine.runAndWait()
            i += 1
        message("Say ready when you're set to cast your vote.")
        response = self.listen_for_ready()
        while response != "ready":
            message("Didn't quite get that")
            message("System ready for your request again")
            response = self.listen_for_ready()
        self.cast_vote()

    def listen_for_ready(self):
        message("listening.....")
        engine = sr.Recognizer()
        with sr.Microphone() as source:
            audio = engine.listen(source)
            try:
                response = engine.recognize_google(audio)
                return response
            except sr.UnknownValueError:
                self.listen_for_ready()
            except sr.RequestError:
                message("Refreshing the system...")
                self.introductory_message()
                self.announce_candidates()

    def cast_vote(self):
        message("Cast your vote now")
        engine = sr.Recognizer()
        with sr.Microphone() as source:
            audio = engine.listen(source)
            try:
                vote = engine.recognize_google(audio)
                # sliced because voter will have to respond with number followed by the actual digit and we want to
                # collect only the digit value
                vote = vote[7:]
                # used because the return from the speech recognition would be in a string word form on the number
                # and we would need to convert to the digit form
                digitVersionOfVote = ttd.Text2Digits()
                # value returned from the text to digits is a string and we need to convert it to int to make some
                # conditions work
                vote = int(digitVersionOfVote.convert(vote))
                # to check for voters who might cast votes for unrecognized candidates
                if vote > self.candidatesNumber:
                    message("Your ballot has been rejected")
                    message("You selected a candidate that does not exist")
                    return
                oldVoteNum = self.fetch_current_vote_num(vote)
                self.record_vote(vote)
                newVoteNum = self.fetch_current_vote_num(vote)
                if newVoteNum > oldVoteNum:
                    message("Vote recorded...")
                    message("Thank you for participating in this election...")
                    message("Enjoy the rest of your day.")
                return
            except sr.UnknownValueError:
                message("Sorry, I did not get that")
                message("Let's try that again")
                self.cast_vote()
            except sr.RequestError:
                message("Could not request services from google at this moment")
                message("Re-running the system...")
                self.introductory_message()
                self.cast_vote()

    def record_vote(self, number):
        currentVote = self.fetch_current_vote_num(number)
        sql = "UPDATE candidates SET Votes = %s WHERE Identifier = %s"
        self.cursor.execute(sql, (currentVote + 1, number, ))
        self.conn.commit()

    def fetch_current_vote_num(self, identifier):
        stmt = "SELECT Votes FROM candidates WHERE Identifier = %s"
        self.cursor.execute(stmt, (identifier,))
        currentVote = self.cursor.fetchall()
        currentVote = currentVote[0][0]
        return currentVote

    def declare_winner(self):
        stmt = "SELECT MAX(Votes) FROM candidates"
        self.cursor.execute(stmt)
        highestVote = self.cursor.fetchall()
        highestVote = highestVote[0][0]
        stmt = "SELECT Name, Party, Votes FROM candidates WHERE Votes = %s"
        self.cursor.execute(stmt, (highestVote,))
        info = self.cursor.fetchall()
        if len(info) > 1:
            message("Candidates")
            for candidate in range(0, len(info)):
                message(f"{info[candidate][0]} of the {info[candidate][1]}, ")
            message("Have tied in the election")
        else:
            winner = info[0][0]
            party = info[0][1]
            votes = info[0][2]
            message(f"{winner} of the {party} has won the election with {votes} votes.")


start = StartVotingSystem(date.today())



