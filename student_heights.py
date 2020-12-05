from collections import defaultdict

"""
a new student creates a new row if none of minimums are taller than him
if the tallest one of out the minimums is still shorter than the new guy, he's gonna create a new row
so approach 2: keep track of the max of the mins and only compare him to the new guy
"""

def increasingRowCount1(a: list) -> int:
    if len(a) == 0:
        return 0
    
    row_shortest = defaultdict(lambda: 10001)  # To keep track of the shortest in each row.
    rows = 1  # There's at least one row, created by the first student.

    row_shortest[1] = a[0]
    a = a[1:]

    for i, height in enumerate(a):
        # Student creates a new row if they can't be the shortest in any of the existing rows
        # If they encounter at least one person taller than them, they join that row
        # If they are taller than all the shortest people, they must create a new row
        joined = False
        for item in row_shortest.items():
            if item[1] > height:
                # join the row, don't increment
                joined = True
                break
        if not joined:
            rows += 1
            row_shortest[rows] = height
            
    return rows

def increasingRowCount2(a: list) -> int:
    if len(a) == 0:
        return 0
    
    row_shortest = [-1, a[0]] # element i is the shortest height in row i, and the rows start at 1
    max_shortest = a[0]
    max_shortest_row = 1
    rows = 1
    a = a[1:]

    for i, height in enumerate(a):
        if max_shortest < height:
            rows += 1
            row_shortest.append(height)
            max_shortest = height
            max_shortest_row = rows
        else:
            # new guy joins an existing row
            # but which row? could be anything we want as long as the shortest in that row is taller than the new guy
            # since max_shortest > height, the new guy can join row number max_shortest_row
            # he becomes the shortest person in that row
            row_shortest[max_shortest_row] = height
            # but since max_shortest is no longer the shortest in his row, we need the new max shortest
            max_shortest = max(row_shortest)
    return rows

a = [5,4,3,1]
ans = increasingRowCount2(a)
print(ans)

"""
You are given an array A representing heights of students. All the students are asked to stand in rows. The students arrive by one, sequentially (as their heights appear in A). For the i-th student, if there is a row in which all the students are taller than A[i], the student will stand in one of such rows. If there is no such row, the student will create a new row. Your task is to find the minimum number of rows created.


Write a function that, given a non-empty array A containing N integers, denoting the heights of the students, returns the minimum number of rows created.


For example, given A = [5, 4, 3, 6, 1], the function should return 2.


Students will arrive in sequential order from A[0] to A[N−1]. So, the first student will have height = 5, the second student will have height = 4, and so on.


For the first student, there is no row, so the student will create a new row.


Row1 = [5]

For the second student, all the students in Row1 have height greater than 4. So, the student will stand in Row1.


Row1 = [5, 4]

Similarly, for the third student, all the students in Row1 have height greater than 3. So, the student will stand in Row1.


Row1 = [5, 4, 3]

For the fourth student, there is no row in which all the students have height greater than 6. So, the student will create a new row.


Row1 = [5, 4, 3]

Row2 = [6]

For the fifth student, all the students in Row1 and Row2 have height greater than 1. So, the student can stand in either of the two rows.


Row1 = [5, 4, 3, 1]

Row2 = [6]

Since two rows are created, the function should return 2.


Assume that:


N is an integer within the range [1..1,000]

each element of array A is an integer within the range [1..10,000]


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment
"""
