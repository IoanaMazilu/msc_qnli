work_days_premise = 20
work_days_hypothesis = 40

# the hypothesis talks about the same work, which is also referenced in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the number of work days in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
