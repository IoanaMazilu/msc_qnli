percentage_required_premise = 40
percentage_required_hypothesis = 50
marks_obtained_premise = 50
marks_obtained_hypothesis = 50
marks_failed_by_premise = 10
marks_failed_by_hypothesis = 10

# the hypothesis talks about the percentage of marks required to clear an exam, and the number of marks obtained and failed by, all referenced also in the premise
if percentage_required_hypothesis <= percentage_required_premise:
    # check if the estimate of 'percentage_required_hypothesis' contradicts the percentage required in the premise
    label = "contradiction"
elif marks_obtained_hypothesis != marks_obtained_premise or marks_failed_by_hypothesis != marks_failed_by_premise:
    # check if the number of marks obtained or failed by in the hypothesis contradicts the number of marks obtained or failed by reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
