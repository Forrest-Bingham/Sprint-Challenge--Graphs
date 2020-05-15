from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

#Create possible moves

# forward_moves = {'n': 'e',
#               'e': 's',
#               's': 'w',
#               'w': None}

backward_moves = {'n' : 's',
                  's' : 'n',
                  'e' : 'w',
                  'w' : 'e' }

#First step
steps = ['n']

#While there is a move, move in that direction, take it off stack
while len(steps) > 0:
    move = steps.pop()
    player.travel(move)

    #If current room has not been visited, add it to traversal

    if player.current_room not in visited_rooms:
        traversal_path.append(backward_moves[move])

        print(f" Added {player.current_room} to traversal path")

        #Add the step back 
        steps.append(backward_moves[move])

        print(f"added {backward_moves[move]} to steps")

        #Update visited room
        visited_rooms.add(player.current_room)
        print(f"added {player.current_room} to visited")

    #Check the next room to see if it is in visited

    for next_move in ["n", "s", "e", "w"]: 

        #move into next room
        new_room = player.current_room.get_room_in_direction(next_move)
        if new_room and new_room not in visited_rooms:

            #Add to traversal path
            traversal_path.append(next_move)

            print(traversal_path, " TRAVERSAL PATH")
            #add move to steps 
            steps.append(next_move)
            print("Steps -- ", steps)
            break

        # player.travel(move)
        # visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
