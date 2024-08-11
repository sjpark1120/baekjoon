import sys
grade_d = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+': 1.5, 'D0':1.0, 'F':0.0}
sum = 0
count = 0
for _ in range(20):
  subject, credit, grade = map(str, sys.stdin.readline().split())
  if grade == 'P':
    continue
  count += float(credit)
  sum += float(credit) * grade_d[grade]
print(sum/count)