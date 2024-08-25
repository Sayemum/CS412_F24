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
    # input_lines = open("E:\\Documents\\VisualStudioCode\\CS412_F24\HW\HW1\\foxsays_t1_in.txt")
    forest_noises = input().split()
    n = int(input())
    animal_phrases = []
    
    for _ in range(n):
        line = input().split()
        animal_phrases.append(line)
    
    
    # create an empty list "fox_says"
    fox_says = []
    also_heard = []
    
    # separate the words in "forest_noises" and loop through each word to check if its in "known_noises"
    #   if true, continue
    #   if false, add it to the list
    for noise in forest_noises:
        noise_exists = False
        
        for entry in animal_phrases:
            animal_name = entry[0]
            animal_noise = entry[2]
            
            if noise == animal_noise:
                if not animal_name in also_heard:
                    also_heard.append(animal_name)
                
                noise_exists = True
                break
            
        if not noise_exists:
            fox_says.append(noise)
    
    # print out the "fox_says" list
    # print out the "known_animal_names" list
    fox_says_str = " "
    also_heard_str = " "
    print("what the fox says: " + fox_says_str.join(fox_says))
    print("also heard: " + also_heard_str.join(also_heard))

if __name__ == "__main__":
    main()
