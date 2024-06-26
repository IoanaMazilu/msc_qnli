dan_hours_worked_premise = 3
dan_hours_worked_hypothesis = 4

# the hypothesis talks about the number of hours Dan worked, referenced also in the premise
if dan_hours_worked_hypothesis != dan_hours_worked_premise:
    # check if the number of hours Dan worked in the hypothesis contradicts the number of hours Dan worked in the premise
    label = "contradiction"
else:
    # if the number of hours Dan worked does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
