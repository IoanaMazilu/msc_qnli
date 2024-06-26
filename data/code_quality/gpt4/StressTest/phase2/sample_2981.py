dan_work_hours_premise = 12
dan_work_hours_hypothesis = 42

# the hypothesis talks about the number of hours Dan works, referenced also in the premise
if dan_work_hours_hypothesis != dan_work_hours_premise:
    # check if the number of hours Dan works in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the number of hours Dan works in the hypothesis does not contradict the number of hours reported in the premise, we can infer entailment
    label = "entailment"

print(label)
