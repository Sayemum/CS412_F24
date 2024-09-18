"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

"""
NOTES:

"""


def backtrack(section_lengths, remaining_height, cache):
    if remaining_height == 0:
        return 0
    if remaining_height < 0:
        return float('inf')
    
    if remaining_height in cache:
        return cache[remaining_height]
    
    min_count = float('inf')
    for section in section_lengths:
        result = backtrack(section_lengths, remaining_height - section, cache)
        if result != float('inf'):
            min_count = min(min_count, result + 1)
    
    cache[remaining_height] = min_count
    return min_count


def find_min_sections(section_lengths, height):
    cache = {}
    result = backtrack(section_lengths, height, cache)
        
    if result != float('inf'):
        return result
    else:
        return -1


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    section_lengths = list(map(int, input().split()))
    height = int(input())
    
    minimum = find_min_sections(section_lengths, height)
    
    print(minimum, "rocket sections minimum")


if __name__ == "__main__":
    main()
