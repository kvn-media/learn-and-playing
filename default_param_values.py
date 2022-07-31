def compute gpa(grades, points={ 'A+' :4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33,
                                 'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
                                 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}):
num courses = 0
total points = 0
for g in grades:
  if g in points:                   # a recognizable grade
    num courses += 1
    total points += points[g]
return total points / num courses