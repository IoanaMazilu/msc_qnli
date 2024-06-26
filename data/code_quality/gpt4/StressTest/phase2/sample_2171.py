percentage_to_pass_premise = 70
percentage_to_pass_hypothesis = 70
marks_obtained_premise = 110
marks_obtained_hypothesis = 110
marks_failed_by_premise = 100
marks_failed_by_hypothesis = 100

# the hypothesis refers to the same marks and percentage as the premise
if percentage_to_pass_hypothesis >= percentage_to_pass_premise:
    # check if the hypothesis value contradicts the premise's percentage to pass
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise:
    # check if the number of marks obtained in the hypothesis contradicts the number of marks obtained reported in the premise
    label = "contradiction"
elif marks_failed_by_hypothesis != marks_failed_by_premise:
    # check if the number of marks failed by in the hypothesis contradicts the number of marks failed by reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
