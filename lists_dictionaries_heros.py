#-------------------------------------------
#
# Objectives:
#Practice writing functions and looping over dictionaries
#Better understand how to traverse through an array of dictionaries or 
#through a dictionary of arrays
# 
#-------------------------------------------


#Problem 1
#Given the information below:

x = [ [5,2,3], [10,8,9] ] 
heros = [{'real_name':  'Bruce Wayne', 'hero_name' : 'Batman'}, {'real_name' : 'Tony Stark', 'hero_name' : 'Ironman'}]
franchise = {
    'dc' : ['Batman', 'Aquaman', 'Wonder Woman', 'Superman'],
    'marvel' : ['Hulk', 'Thor', 'Black Widow']
}
z = [ {'x': 10, 'y': 20} ]

#1.) How would you change the value 10 in x to 15?  Once you're done x should then be [ [5,2,3], [15,8,9] ].  

for i in range(len(x)):
    for j in range(i):
        if x[i][j] == 10:
            x[i][j] = 15
print(x)

#2.) How would you change the hero_name of the first hero from 'Batman' to "Dark Knight"?

heros[0]['hero_name'] = "Dark Knight"
print(heros)

#3.) For the franchise dictionary, how would you change 'Aquaman' to 'Daredevil'?
franchise['dc'][1] = 'Daredevil'
print(franchise)
#4.) For z, how would you change the value 20 to 30?
z[0]['y'] = 30
print(z)
#-----------------------------------------------------------------

#Problem 2
#Create a function that given a list of dictionaries, it loops through each dictionary in the list and prints each key and the associated value.  
#For example, given the following list:

superheros = [
    {'real_name': 'Steve Rogers', 'hero_name': 'Captain America'},
    {'real_name': 'Barry Allan', 'hero_name': 'The Flash'},
    {'real_name': 'Bruce Banner', 'hero_name': 'The Incredible Hulk'},
    {'real_name': 'Diana Prince', 'hero_name': 'Wonder Woman'}
]

#iterateDictionary(superheros) should output

#real_name - Steve Rogers, hero_name - Captain America
#real_name - Barry Allan, hero_name - The Flash
#real_name - Bruce Banner, hero_name - The Incredible Hulk 
#real_name - Diana Prince, hero_name - Wonder Woman


def iterateDictionary(superheros):
    for hero in superheros:
        for key,value in hero.items():
            print(key+ '-' +value, end =', ')
            print()
iterateDictionary(superheros)



#------------------------------------------------------------------
#Problem 3
#Create a function that given a list of dictionaries and a key name, 
#it outputs the value stored in that key for each dictionary.  
#For example, iterateDictionary2('real_name', superheros) should output

#Steve Rogers
#Barry Allan
#Bruce Banner
#Diana Prince

def iterateDictionary2(str, superheros):
    for hero in superheros:
        print(hero[str])
iterateDictionary2('real_name', superheros)


#-----------------------------------------------------------------
#Problem 4
#Create a function that prints the name of each disney and pixar movie and also how many movies each category currently has.
#Note the output formatting
movie_collection = {
    'disney': ['Cinderella', 'Encanto', 'Little Mermaid', 'Tangled', 'Beauty & The Beast', 'Lion King', '101 Dalmations'],
    'pixar': ['Toy Story', 'Monsters, Inc.', 'Up', 'Finding Nemo', 'Coco', 'Wall-E', 'The Incredibles', 'Inside Out']
}

def count_list(movie_collection):
    for movie, collection in movie_collection.items():
        print(len(movie) +1, end= " ")
        print( movie.upper())
        for movie_name in collection:
            print(movie_name)
        print()
count_list(movie_collection)

#Expected Outpout
#7 DISNEY
#- Cinderella
#- Encanto
#- Little Mermaid
#- Tangled
#- Beauty & The Beast
#- Lion King
#- 101 Dalmations
    
#8 PIXAR
#-Toy Story
#-Monsters, Inc.
#-Up
#-Finding Nemo
#-Coco
#-Wall-E
#-The Incredibles
#-Inside Out
