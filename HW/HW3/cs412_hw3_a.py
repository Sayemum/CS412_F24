"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

"""
NOTES:

"""

def backtrack(section_lengths, remaining_height, count):
    if remaining_height == 0:
        return count
    if remaining_height < 0:
        return float('inf')
    
    min_count = float('inf')
    for section in section_lengths:
        result = backtrack(section_lengths, remaining_height - section, count + 1)
        min_count = min(min_count, result)
    
    return min_count


def find_min_sections(section_lengths, height):
    result = backtrack(section_lengths, height, 0)
    
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
    
    print(section_lengths)
    print(height)
    
    minimum = find_min_sections(section_lengths, height)
    
    print(minimum, "rocket sections minimum")


if __name__ == "__main__":
    main()
