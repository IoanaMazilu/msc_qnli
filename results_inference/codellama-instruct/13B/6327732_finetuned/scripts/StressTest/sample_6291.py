marks_english_premise = 76
marks_maths_premise = 65
marks_chemistry_premise = 82
marks_biology_premise = 67
marks_physics_premise = 85

marks_english_hypothesis = 46
marks_maths_hypothesis = 65
marks_chemistry_hypothesis = 82
marks_biology_hypothesis = 67
marks_physics_hypothesis = 85

# the hypothesis refers to the number of marks obtained in each subject, mentioned in the premise
if marks_english_hypothesis <= marks_english_premise:
    # check if the estimate of'marks_english_hypothesis' contradicts the number of marks in English in the premise
    label = "contradiction"
elif marks_maths_hypothesis!= marks_maths_premise:
    # check if the number of marks in Mathematics in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_chemistry_hypothesis!= marks_chemistry_premise:
    # check if the number of marks in Chemistry in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_biology_hypothesis!= marks_biology_premise:
    # check if the number of marks in Biology in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
elif marks_physics_hypothesis!= marks_physics_premise:
    # check if the number of marks in Physics in the hypothesis contradicts the number of marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
