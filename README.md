# pokemoncalculator
A Python script that calculates the defensive capabilities of any given Pokemon team and maps it out onto a spreadsheet.
How the script works is that it starts off by initialisiing the different pokemon type effectiveness by assigning each type to a list
The list consists of integers showing each type's effectiveness on the specific type
e.g fighting type = fighting = [1,1,2,1,1,0.5,0.5,1,1,1,1,1,1,2,1,1,0.5,2]
In order of: normal, fighting, flying, poison, ground, rock, bug, ghost, steel, fire, water, grass, electric, psychic, ice, dragon, dark, fairy
Normal and Fighting attacks do 1x damage, flying type attacks do 2x damage, etc

The lists will then be assigned to a dictionary for easier retrieval.
There will be a function called typecalculation() which contains 2 nested functions, typeinput and typeability.
typeinput() takes in the user's input of the 2 types per pokemon
typeability() takes into account any type-effectiveness-altering ability the pokemon might have (e.g flash fire).

The main code runs as such:
1. Get the user to input the number of pokemon in a team
2. Go into the for loop where the process iterates over the number of pokemon in the team
3. Go to the typecalculation() function
4. Calculate the TOTAL type effectiveness of the whole team
5. Append the information to a dictionary, where the keys are the pokemon names and the values are the type effectiveness values
6. Convert the dictionary to a DataFrame object using pandas
7. Save the DataFrame to a csv file

Have fun!
