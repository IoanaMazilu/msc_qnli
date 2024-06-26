english_marks = 86
mathematics_marks = 85
physics_marks = 82
chemistry_marks = 87
biology_marks = 85

average_marks = (english_marks + mathematics_marks + physics_marks + chemistry_marks + biology_marks) / 5

if average_marks < 86:
    label = "entailment"
elif average_marks > 86:
    label = "contradiction"
else:
    label = "neutral"

print(label)
