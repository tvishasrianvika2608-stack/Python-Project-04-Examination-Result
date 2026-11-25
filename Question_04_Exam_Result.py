
n = int(input("Enter number of subjects: "))

marks = []
grace_used = 0
total = 0

for i in range(n):
    mark = int(input("Enter marks for subject " + str(i + 1) + ": "))

    if mark < 0 or mark > 100:
        print("Invalid marks!")
        exit()

    if mark < 40 and mark >= 35:
        needed = 40 - mark

        if grace_used + needed <= 5:
            mark = mark + needed
            grace_used = grace_used + needed

    marks.append(mark)
    total = total + mark

print("\n----- EXAMINATION RESULT -----")

for i in range(n):
    print("Subject", i + 1, ":", marks[i])

percentage = total / n

print("Total Marks:", total, "/", n * 100)
print("Grace Marks Used:", grace_used)
print("Percentage:", percentage)

if any(mark < 40 for mark in marks):
    print("Result: FAIL")
else:
    if percentage >= 75:
        print("Result: DISTINCTION")
    elif percentage >= 60:
        print("Result: FIRST CLASS")
    elif percentage >= 50:
        print("Result: SECOND CLASS")
    else:
        print("Result: PASS")

print("------------------------------")
