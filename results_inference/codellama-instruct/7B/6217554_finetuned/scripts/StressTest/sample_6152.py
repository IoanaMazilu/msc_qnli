total_hours_worked_premise = 41
total_hours_worked_hypothesis = 11

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if total_hours_worked_hypothesis!= total_hours_worked_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
