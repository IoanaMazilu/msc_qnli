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
if marks_english_hypothesis > marks_english_premise:
    # check if the hypothesis value contradicts the premise value for English marks
    label = "contradiction"
elif marks_mathematics_hypothesis > marks_mathematics_premise:
    # check if the hypothesis value contradicts the premise value for Mathematics marks
    label = "contradiction"
elif marks_chemistry_hypothesis > marks_chemistry_premise:
    # check if the hypothesis value contradicts the premise value for Chemistry marks
    label = "contradiction"
elif marks_biology_hypothesis > marks_biology_premise:
    # check if the hypothesis value contradicts the premise value for Biology marks
    label = "contradiction"
elif marks_physics_hypothesis > marks_physics_premise:
    # check if the hypothesis value contradicts the premise value for Physics marks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)