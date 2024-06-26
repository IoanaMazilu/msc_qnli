marks_english_premise = 96
marks_mathematics_premise = 95
marks_physics_premise = 82
marks_chemistry_premise = 87
marks_biology_premise = 92

marks_english_hypothesis = 96
marks_mathematics_hypothesis = 95
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 92

# the hypothesis refers to the marks obtained in each subject, which are also mentioned in the premise
if marks_english_hypothesis > marks_english_premise:
    # check if the hypothesis value contradicts the premise value for English marks
    label = "contradiction"
elif marks_mathematics_hypothesis > marks_mathematics_premise:
    # check if the hypothesis value contradicts the premise value for Mathematics marks
    label = "contradiction"
elif marks_physics_hypothesis > marks_physics_premise:
    # check if the hypothesis value contradicts the premise value for Physics marks
    label = "contradiction"
elif marks_chemistry_hypothesis > marks_chemistry_premise:
    # check if the hypothesis value contradicts the premise value for Chemistry marks
    label = "contradiction"
elif marks_biology_hypothesis > marks_biology_premise:
    # check if the hypothesis value contradicts the premise value for Biology marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
