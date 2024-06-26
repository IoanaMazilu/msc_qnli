james_worked_premise = 41
james_worked_hypothesis = 61

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if james_worked_hypothesis!= james_worked_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)