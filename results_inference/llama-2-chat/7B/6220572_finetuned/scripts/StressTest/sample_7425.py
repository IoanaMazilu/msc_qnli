marks_english_premise = 85
marks_mathematics_premise = 86
marks_physics_premise = 82
marks_chemistry_premise = 67
marks_biology_premise = 85

# the hypothesis refers to the marks obtained in different subjects as mentioned in the premise
if marks_english_hypothesis >= marks_english_premise or marks_mathematics_hypothesis >= marks_mathematics_premise or marks_physics_hypothesis >= marks_physics_premise or marks_chemistry_hypothesis >= marks_chemistry_premise or marks_biology_hypothesis >= marks_biology_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of marks
    # any number of marks less than the premise ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
