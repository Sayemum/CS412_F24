def subset_sum(subset, i, target):
    if target == 0:
        return True
    if target < 0 or i == len(subset):
        return False
    
    withx = subset_sum(subset, i + 1, target - subset[i])
    withoutx = subset_sum(subset, i + 1, target)
    
    return withx or withoutx

def main():
    target = 10
    subset = [2, 2, 2, 3, 2, 2]
    
    print(subset_sum(subset, 0, target))


if __name__ == "__main__":
    main()
