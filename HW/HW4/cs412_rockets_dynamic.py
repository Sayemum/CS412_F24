"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

"""
NOTES:

"""


def find_min_sections(section_lengths, height):
    cache = [float('inf')] * (height + 1)
    cache[0] = 0
    
    # Fill the array
    for i in range(1, height + 1):
        for section in section_lengths:
            if (i - section >= 0) and (cache[i - section] != float('inf')):
                cache[i] = min(cache[i], cache[i - section] + 1)
    
    if cache[height] == float('inf'):
        return -1
    
    # Find solution by tracing back
    current_height = height
    while current_height > 0:
        for section in section_lengths:
            if (current_height - section >= 0) and (cache[current_height] == cache[current_height - section] + 1):
                current_height -= section
                break
    
    return cache[height]


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
