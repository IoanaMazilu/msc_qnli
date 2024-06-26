# the premise gives the marks obtained by David in each subject
english_marks = 86
mathematics_marks = 85
physics_marks = 87
chemistry_marks = 85
biology_marks = 82

# the hypothesis gives the marks obtained by David in each subject
hypothesis_marks = [16, 85, 82, 87, 85]

# the hypothesis contradicts the premise because the marks in the hypothesis are less than the marks in the premise
if english_marks < 16 or mathematics_marks < 85 or physics_marks < 87 or chemistry_marks < 85 or biology_marks < 82:
    label = "contradiction"
else:
    label = "neutral"

print(label)
