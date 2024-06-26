y - 25

work_days_premise = 25
work_days_hypothesis = 25

# the hypothesis talks about the number of days it takes to complete a work, which is also mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis does not contradict the number of days in the premise, we can infer entailment
    label = "entailment"

print(label)
