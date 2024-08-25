"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
def main():
    # your code here
    # pass
    
    # Grab imported input txt file
    # input_lines = open("E:\\Documents\\VisualStudioCode\\CS412_F24\HW\HW1\\foxsays_t1_in.txt")
    input_lines = open("E:\\Documents\\VisualStudioCode\\CS412_F24\HW\HW1\\foxsays_t2_in.txt")
    
    # split every line with \n into a list of lines
    # lines = input_file.split
    # for line in input_file:
    #     print(line)
    # print(type(input_lines))
    input_list_raw = list(input_lines)
    input_list = list(map(lambda line: line[:-1:], input_list_raw)) # removes the \n at the end of each line
    # print(input_list)
    # print(input_list_trunc)
    
    # break each line into: 1.) forest_noises, 2.) total_known_sounds, 3.) animal_phrases [List]
    forest_noises = input_list[0].split()
    total_known_sounds = input_list[1]
    animal_phrases = input_list[2 : len(input_list)-1] # ignore the "what fox says" line at the end
    # print(forest_noises)
    # print(total_known_sounds)
    # print(animal_phrases)
    
    
    # create an list "known_noises" that takes every noise from each known animal after "[animal] goes " like "woof" and "blub" and put it in the list
    # do the exact same thing but for a list of known animal names "known_animal_names" like "dog" and "fish"
    known_noises = []
    known_animal_names = []
    
    for phrase in animal_phrases:
        words = phrase.split()
        
        known_animal_names.append(words[0])
        known_noises.append(words[2])
            
    
    # create an empty list "fox_says"
    fox_says = []
    
    # separate the words in "forest_noises" and loop through each word to check if its in "known_noises"
    #   if true, continue
    #   if false, add it to the list
    for noise in forest_noises:
        if noise in known_noises:
            continue
        else:
            fox_says.append(noise)
    
    # print out the "fox_says" list
    # print out the "known_animal_names" list
    # print(fox_says)
    # print(known_animal_names)
    fox_says_str = " "
    known_animal_names_str = " "
    print("what the fox says: " + fox_says_str.join(fox_says))
    print("also heard: " + known_animal_names_str.join(known_animal_names))
    
    input_lines.close()

if __name__ == "__main__":
    main()
