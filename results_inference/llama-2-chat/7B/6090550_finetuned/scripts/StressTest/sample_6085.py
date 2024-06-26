work_days_premise = 10
work_days_hypothesis = 20

# the hypothesis talks about the number of days to complete a piece of work, which is also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
