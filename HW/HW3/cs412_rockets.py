"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

"""
NOTES:

"""


def backtrack(section_lengths, remaining_height, length_to_count, count):
    if remaining_height == 0:
        return count
    if remaining_height < 0:
        return float('inf')
    
    min_count = float('inf')
    for section in section_lengths:
        result = backtrack(section_lengths, remaining_height - section, length_to_count, count + 1)
        min_count = min(min_count, result)
        
        #if section not in length_to_count:
        length_to_count[section] = min_count
    
    return min_count


def find_min_sections(section_lengths, height, length_to_count):
    result = backtrack(section_lengths, height, length_to_count, 0)
    
    if result != float('inf'):
        return result
    else:
        return -1


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    section_lengths = [1, 2, 5, 7]
    height = 15
    # section_lengths = list(map(int, input().split()))
    # height = int(input())
    
    length_to_count = {}
    
    # print(section_lengths)
    # print(height)
    
    minimum = find_min_sections(section_lengths, height, length_to_count)
    
    print(minimum, "rocket sections minimum")
    print()
    print(length_to_count)


if __name__ == "__main__":
    main()
