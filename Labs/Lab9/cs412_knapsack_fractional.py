"""
    name:  Sayemum Hassan

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.

           Comments here on your code and submission.
"""


def main():
    # get input
    
    w = int(input())
    n = int(input())
    
    triples = []
    for _ in range(n):
        line = input().split()
        triples.append([line[0], float(line[1]), float(line[2])])
    
    triples.sort(key=lambda x: (x[1] / x[2]), reverse=True)
    
    total = 0.0
    taken_items = []
    
    for item in triples:
        if item[2] <= w:
            w -= item[2]
            total += item[1]
            taken_items.append((item[0], item[1], item[2]))
        else:
            frac_profit = item[1] * (w / item[2])
            total += frac_profit
            taken_items.append((item[0], frac_profit, w))
            break
    
    outputs = [f"{item[0]}({item[1]:.2f}, {item[2]:.2f})" for item in taken_items]
    print(" ".join(outputs))
    print(total)

if __name__ == "__main__":
    main()
