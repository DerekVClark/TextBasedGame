#Derek Clark

#A dictionary linking a room to other rooms
#and linking one item for each room except the Start room (Start) and the room containing the villain
rooms = {
   'Start' : { 'East' : 'Library'},
   'Library' : { 'North' : 'Blacksmith', 'East' : 'Kitchen','South' : 'Armory', 'West' : 'Start' , 'item' : 'Library key' },
   'Armory' : { 'East' : 'Bathroom', 'North' : 'Library', 'item' : 'Sword' },
   'Bathroom' : { 'North' : 'Kitchen', 'West' : 'Armory', 'item' : 'Bathroom key' },
   'Kitchen' : {'North' : 'Throne room', 'South' : 'Bathroom', 'West' : 'Library', 'item' : 'Kitchen key'},
   'Blacksmith' : {'South' : 'Library', 'East' : 'Prince room', 'item' : 'Armor'},
   'Prince room' : {'West' : 'Blacksmith', 'item' : 'Prince room key'},
   'Throne room' : {'South' : 'Kitchen', 'item' : 'king'} # villan
}

#Print instructions on how to play the game
def instructions():
    print('#########################################################')
    print('##### Traverse the map by typing directions such as #####')
    print('#####       South | North | East | West             #####')
    print('#####   If INVALID please select a new direction    #####')
    print("#####       Add to Inventory: get 'item name'       #####")
    print('#####    Collect all 6 items then make your way     #####')
    print('#####        to the cellar to win the game!         #####')
    print('#########################################################')


#Status function that take the location of the player and the current inventory and prints it
def status(location, inventory):
    print('######################################################')
    print('You are in', location)
    print('Inventory: ',inventory)
    print('------------------------------------------------------')
    
#runs instruction function
instructions()

#Main game function
def main():
    inventory = [] #Initializes the inventory with an empty list

    current_room = 'Start' #Initializes player start point

    while True: #Main loop
        status(current_room,inventory) #Prints status each time player interacts or moves
        print('Please tell me the direction in which you would like to move:')
        move = str(input()).capitalize() #Capitalize to make sure the answer can be entered lowercase
        if move in rooms[current_room] and current_room != 'Kitchen': # Checks if the user input is in the current room
            current_room = (rooms[current_room][move]) #Sets current room to the one with the direction
        elif move == 'Status': #If player enters status it prints the status
            status(current_room, inventory)

        elif current_room == 'Kitchen' and move == 'North' and len(inventory) < 6: #Replacable with break for lose condition instead informs player to find 6 items and continues loop
            print('You need to get all 6 items first')
        elif current_room == 'Kitchen' and move == 'North' and len(inventory) >= 6: #Win condition if player has 6 items he may proceed to kill the king
            current_room = (rooms[current_room][move])
            status(current_room,inventory)
            print('Would you like to defeat the king?')
            win = str(input()).capitalize()
            if win == 'Yes': #If input yes win game and break code
                print('You win!')
                break
            else:
                current_room = 'Kitchen' #If no bring player back to kitchen

        elif current_room == 'Kitchen' and move == 'West': #Seperates the movement from kitchen so that no errors occur moving west
            current_room = (rooms[current_room][move])
            status(current_room,inventory)
        elif current_room == 'Kitchen' and move == 'South':#Seperates the movement from kitchen so that no errors occur moving south
            current_room = (rooms[current_room][move])
            status(current_room,inventory)

        else:
            print('Invalid direction!') #Invalid direction
            
    


        while current_room != 'Start' and 'item' in (rooms[current_room]) and current_room != 'Throne room': #Loop for grabbing items as long as not in final boss room and makes sure item isnt already in inventory
            print('You see a', (rooms[current_room]['item']), 'would you like to pick it up?')
            grab = str(input()).capitalize()
            if grab == 'Yes': #Takes item adds it to inventory and removes it from the dictionary so loop does not come up again
                inventory.append(rooms[current_room]['item'])
                print("You've picked up the", (rooms[current_room]['item']))
                del (rooms[current_room]['item'])
                print('------------------------------------------------------')
            elif grab == 'No': #Leaves item and breaks loop so player can move again
                print('You left the item!')
                print('------------------------------------------------------')
                break
            else:
                print('Invalid')

main()


#Optional code to make the player lose instead of replying to the player with you need to obtain 6 items and continuing the loop you can reply with you lose and break to end the code