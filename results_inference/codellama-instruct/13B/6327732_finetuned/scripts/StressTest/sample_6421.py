marks_english_premise = 66
marks_maths_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85

marks_english_hypothesis = 76
marks_maths_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85

# the hypothesis refers to the exact marks obtained by Arun in each subject, as mentioned in the premise
if marks_english_hypothesis!= marks_english_premise or marks_maths_hypothesis!= marks_maths_premise or marks_chemistry_hypothesis!= marks_chemistry_premise or marks_biology_hypothesis!= marks_biology_premise or marks_physics_hypothesis!= marks_physics_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # the premise gives exact values for the marks obtained by Arun in each subject
    # any number of marks greater than or equal to the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
