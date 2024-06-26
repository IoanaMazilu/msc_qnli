# marks obtained by Arun in each subject
english_marks = 76
mathematics_marks = 65
chemistry_marks = 82
biology_marks = 67
physics_marks = 85

# hypothesis: more than 66, 65, 82, 67 and 85 marks
hypothesis_marks = 66
hypothesis_marks_chemistry = 65
hypothesis_marks_biology = 67
hypothesis_marks_physics = 85

# check if the hypothesis marks contradict the premise marks
if english_marks <= hypothesis_marks:
    label = "contradiction"
elif mathematics_marks <= hypothesis_marks_mathematics:
    label = "contradiction"
elif chemistry_marks <= hypothesis_marks_chemistry:
    label = "contradiction"
elif biology_marks <= hypothesis_marks_biology:
    label = "contradiction"
elif physics_marks <= hypothesis_marks_physics:
    label = "contradiction"
else:
    label = "entailment"

print(label)
