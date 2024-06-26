marks_english_premise = 16
marks_maths_premise = 95
marks_physics_premise = 82
marks_chemistry_premise = 87
marks_biology_premise = 92

marks_english_hypothesis = 96
marks_maths_hypothesis = 95
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 87
marks_biology_hypothesis = 92

# the hypothesis refers to the marks obtained in each subject, which are also mentioned in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the number of marks in the premise
    label = "contradiction"
elif marks_maths_hypothesis!= marks_maths_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_physics_hypothesis!= marks_physics_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis!= marks_chemistry_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_biology_hypothesis!= marks_biology_premise:
    # check if the number of marks in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)