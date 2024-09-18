"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""

"""
NOTES:

"""


def backtrack(section_lengths, remaining_height, count, section_counts, memo):
    if remaining_height == 0:
        return count, section_counts.copy()
    if remaining_height < 0:
        return float('inf'), section_counts
    
    if remaining_height in memo:
        return memo[remaining_height]
    
    min_count = float('inf')
    min_section_counts = {}
    for section in section_lengths:
        section_counts[section] += 1
        
        result, current_counts = backtrack(section_lengths, remaining_height - section, count + 1, section_counts, memo)
        
        section_counts[section] -= 1
        
        if result < min_count:
            min_count = result
            min_section_counts = current_counts
    
    memo[remaining_height] = (min_count, min_section_counts)
    return min_count, min_section_counts


def find_min_sections(section_lengths, height):
    section_counts = {length: 0 for length in section_lengths}
    memo = {}
    
    result, length_to_count = backtrack(section_lengths, height, 0, section_counts, memo)
    
    if result != float('inf'):
        return result, length_to_count
    else:
        return -1, {}


def main():
    # get input
    # section_lengths = [1, 2, 5, 7]
    # height = 15
    section_lengths = list(map(int, input().split()))
    height = int(input())
    
    minimum, length_to_count = find_min_sections(section_lengths, height)
    
    for length in sorted(length_to_count.keys()):
        print(length_to_count[length], "of length", length)
    
    print(minimum, "rocket sections minimum")


if __name__ == "__main__":
    main()
