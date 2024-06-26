marks_english_premise = 86
marks_maths_premise = 89
marks_physics_premise = 82
marks_chemistry_premise = 87
marks_biology_premise = 81

marks_english_hypothesis = 56
marks_maths_hypothesis = 89
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 81

# the hypothesis refers to the marks obtained in the same subjects as the premise
if marks_english_hypothesis <= marks_english_premise and marks_maths_hypothesis <= marks_maths_premise and marks_physics_hypothesis <= marks_physics_premise and marks_chemistry_hypothesis <= marks_chemistry_premise and marks_biology_hypothesis <= marks_biology_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives the exact marks obtained in each subject
    # any number of marks greater than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
