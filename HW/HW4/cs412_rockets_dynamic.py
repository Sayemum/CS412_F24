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
    
    section_count = [[0] * len(section_lengths) for _ in range(height + 1)]
    
    # Fill the array
    for i in range(1, height + 1):
        for j, section in enumerate(section_lengths):
            if i - section >= 0 and cache[i - section] != float('inf'):
                if cache[i] > cache[i - section] + 1:
                    cache[i] = cache[i - section] + 1
                    section_count[i] = section_count[i - section][:]
                    section_count[i][j] += 1
    
    if cache[height] == float('inf'):
        return -1, []
    
    return cache[height], section_count[height]


def main():
    # get input
    # n = 3
    # remove_coords = (0, 0)
    section_lengths = list(map(int, input().split()))
    height = int(input())
    
    minimum, used_sections = find_min_sections(section_lengths, height)

    for i, count in enumerate(used_sections):
        print(count, "of length", section_lengths[i])
    
    print(minimum, "rocket sections minimum")


if __name__ == "__main__":
    main()
