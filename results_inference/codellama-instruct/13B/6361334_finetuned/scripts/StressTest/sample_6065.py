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
if marks_english_hypothesis!= marks_english_premise or marks_maths_hypothesis!= marks_maths_premise or marks_physics_hypothesis!= marks_physics_premise or marks_chemistry_hypothesis!= marks_chemistry_premise or marks_biology_hypothesis!= marks_biology_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
