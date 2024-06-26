marks_english_premise = 86
marks_mathematics_premise = 85
marks_physics_premise = 82
marks_chemistry_premise = 87
marks_biology_premise = 85

marks_english_hypothesis = 86
marks_mathematics_hypothesis = 85
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 85

# the hypothesis refers to the marks obtained in the subjects mentioned in the premise
if marks_english_hypothesis > marks_english_premise or marks_mathematics_hypothesis > marks_mathematics_premise or marks_physics_hypothesis > marks_physics_premise or marks_chemistry_hypothesis > marks_chemistry_premise or marks_biology_hypothesis > marks_biology_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives the exact marks obtained in each subject
    # any number of marks less than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
