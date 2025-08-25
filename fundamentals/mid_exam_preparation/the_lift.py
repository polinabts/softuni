# people = int(input())
# lift_state_str = input().split()
#
# # cast the string elements in the list to integers
# lift_list_ints: list = list(map(int, lift_state_str))
#
# # max people per wagon
# wagon_limit = 4
#
# for index, wagon in enumerate(lift_list_ints):
#     # check if there is a place on the wagon, if so-fill it
#     if wagon < wagon_limit and people > 0:
#         # calculate the free seats
#         free_seats = wagon_limit - wagon
#         if people - free_seats >= 0:
#             # calculate remaining people
#             people -= free_seats
#             # fill the wagon to limit
#             new_wagon = wagon_limit
#         else:
#             # there are not enough people to fill the wagon, just add the remaining people
#             new_wagon = wagon + people
#         # replace the wagon in the list with the calculated new_wagon
#         lift_list_ints[index] = new_wagon
#
# print(f"remaining people: {people}")
# print(f"lift status: {lift_list_ints}")


waiting_people = int(input())
state_of_lift = input().split()

state_of_lift_as_integer = list(map(int, state_of_lift))

