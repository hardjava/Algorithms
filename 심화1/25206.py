a = {
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}

sumGrade = 0
sumUnit = 0
for i in range(20):
    subject, unit, grade = map(str, input().split())
    if grade != 'P':
        value = float(unit) * a[grade]
        sumGrade += value
        sumUnit += float(unit)

print(sumGrade / sumUnit)
