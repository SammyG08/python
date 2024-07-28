import database_and_processes

coffee_resources_done = False
not_enough_resources_printed = 0

print(database_and_processes.coffee_making_resources)

while not coffee_resources_done:
    not_enough_resources_printed += database_and_processes.processing_order()
    if not_enough_resources_printed > 5:
        coffee_resources_done = True

print(database_and_processes.coffee_making_resources)