"""
    name: Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def is_indep_set(edge_list, indep_set):
    for vertex in indep_set:
        for neighbor in edge_list[vertex]:
            if neighbor in indep_set:
                return False
    
    return True


def main():
    # get input
    num_vertices = int(input())
    edge_list = {i: [] for i in range(num_vertices)}
    
    for i in range(num_vertices):
        edges = input().split()
        edge_list[i] = [int(edge) for edge in edges]
    
    
    set_input = input().split()
    indep_set = set([int(edge) for edge in set_input])
    
    if is_indep_set(edge_list, indep_set):
        print("TRUE")
    else:
        print("FALSE")


if __name__ == "__main__":
    main()
