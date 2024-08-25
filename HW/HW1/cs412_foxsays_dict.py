"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    
    # Grab imported input txt file
    forest_noises = input().split()
    n = int(input())
    animal_phrases = []
    
    for _ in range(n):
        line = input().split()
        animal_phrases.append(line)
    
    # # create an list "known_noises" that takes every noise from each known animal after "[animal] goes " like "woof" and "blub" and put it in the list
    # # do the exact same thing but for a list of known animal names "known_animal_names" like "dog" and "fish"
    known_animal_noises = {} # use a dictionary instead of 2 lists
    
    for phrase in animal_phrases:
        # animal_name = words[0]
        # animal_noise = words[2]
        
        known_animal_noises[phrase[2]] = phrase[0]
    
    # create an empty list "fox_says"
    fox_says = []
    also_heard = []
    
    # separate the words in "forest_noises" and loop through each word to check if its in "known_noises"
    #   if true, continue
    #   if false, add it to the list
    for noise in forest_noises:
        
        animal_name = known_animal_noises.get(noise)
        if animal_name != None:
            if not animal_name in also_heard:
                also_heard.append(animal_name)
        else:
            fox_says.append(noise)
    
    
    # print out the "fox_says" list
    # print out the "known_animal_names" list
    fox_says_str = " "
    also_heard_str = " "
    print("what the fox says: " + fox_says_str.join(fox_says))
    print("also heard: " + also_heard_str.join(also_heard))

if __name__ == "__main__":
    main()
