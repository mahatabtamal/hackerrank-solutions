if __name__ == '__main__':
    # The first part is obvious
    n = int(input())
    students = []  

    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score]) # Append the name and score as a sublist

    # Get all unique scores and sort them to find the second lowest
    # We use a set comprehension to get unique scores, then sort them
    sorted_unique = sorted({score for name, score in students})

    # The second lowest score will be at index 1
    if len(sorted_unique) < 2:
        print("No second lowest.")
    else:
        second_lowest = sorted_unique[1]

        # Collect all names with the second lowest score
        # then sort and print them
        second_lowest_people = []
        for name, score in students:
            if score == second_lowest:
                second_lowest_people.append(name)

        # Print the names in alphabetical order
        for name in sorted(second_lowest_people):
            print(name)
