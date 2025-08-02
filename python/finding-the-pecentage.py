if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        # first elem to name, the rest to another list
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    if query_name in student_marks:
        scores = student_marks[query_name]
        total_score = sum(scores)
        avg = total_score / len(scores)
        print(f"{avg:.2f}")
    
    
