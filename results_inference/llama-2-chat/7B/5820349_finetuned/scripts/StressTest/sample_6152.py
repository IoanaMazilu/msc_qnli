james_hours_worked_premise = 41
james_hours_worked_hypothesis = 11

# the hypothesis talks about the number of hours James worked last week, referenced also in the premise
if james_hours_worked_hypothesis!= james_hours_worked_premise:
    # check if the number of hours James worked in the hypothesis contradicts the number of hours James worked reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
