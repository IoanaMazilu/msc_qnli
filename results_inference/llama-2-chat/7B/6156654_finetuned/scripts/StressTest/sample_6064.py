marks_english = 86
marks_mathematics = 89
marks_physics = 82
marks_chemistry = 87
marks_biology = 81

# the hypothesis refers to the marks obtained by Dacid in different subjects
if marks_english!= 89 or marks_mathematics!= 89 or marks_physics!= 82 or marks_chemistry!= 87 or marks_biology!= 81:
    # check if any of the marks in the hypothesis contradicts the marks in the premise
    label = "contradiction"
else:
    # if all the marks in the hypothesis are the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
