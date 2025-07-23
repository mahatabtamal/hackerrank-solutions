if __name__ == '__main__':

    n = int(input())

    students = dict()

    for _ in range(n):
        name = input()
        score = float(input())

        students.update({name: score})
        sorted_students = sorted(set(students.values))

        for i in sorted(students):
            if students[i] == sorted_students[1]:
                print(i)
        
