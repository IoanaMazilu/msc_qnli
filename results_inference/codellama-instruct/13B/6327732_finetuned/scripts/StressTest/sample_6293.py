marks_english_premise = 76
marks_mathematics_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85

marks_english_hypothesis = 76
marks_mathematics_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85

# the hypothesis refers to the marks obtained in each subject, which are also mentioned in the premise
if marks_english_hypothesis <= marks_english_premise and marks_mathematics_hypothesis <= marks_mathematics_premise and marks_chemistry_hypothesis <= marks_chemistry_premise and marks_biology_hypothesis <= marks_biology_premise and marks_physics_hypothesis <= marks_physics_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives the exact marks obtained in each subject
    # any number of marks less than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
