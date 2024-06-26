marks_english_premise = 76
marks_english_hypothesis = 76
marks_mathematics_premise = 65
marks_mathematics_hypothesis = 65
marks_physics_premise = 82
marks_physics_hypothesis = 82
marks_chemistry_premise = 67
marks_chemistry_hypothesis = 67
marks_biology_premise = 85
marks_biology_hypothesis = 85

# the hypothesis refers to the marks obtained in each subject mentioned in the premise
if marks_english_hypothesis >= marks_english_premise or marks_mathematics_hypothesis >= marks_mathematics_premise or marks_physics_hypothesis >= marks_physics_premise or marks_chemistry_hypothesis >= marks_chemistry_premise or marks_biology_hypothesis >= marks_biology_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
