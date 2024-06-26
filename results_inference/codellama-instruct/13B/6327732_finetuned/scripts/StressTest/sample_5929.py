marks_english_premise = 46
marks_mathematics_premise = 85
marks_physics_premise = 92
marks_chemistry_premise = 87
marks_biology_premise = 95

marks_english_hypothesis = 86
marks_mathematics_hypothesis = 85
marks_physics_hypothesis = 92
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 95

# the hypothesis refers to the marks obtained in each subject, mentioned in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_mathematics_hypothesis <= marks_mathematics_premise:
    # check if the estimate of'marks_mathematics_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_physics_hypothesis <= marks_physics_premise:
    # check if the estimate of'marks_physics_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis <= marks_chemistry_premise:
    # check if the estimate of'marks_chemistry_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_biology_hypothesis <= marks_biology_premise:
    # check if the estimate of'marks_biology_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
