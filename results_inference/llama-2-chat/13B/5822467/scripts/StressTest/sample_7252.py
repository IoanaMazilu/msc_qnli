suraj_runs_premise = 5
suraj_runs_hypothesis = 8

# the hypothesis refers to the number of innings played by Suraj
if suraj_runs_hypothesis <= suraj_runs_premise:
    # check if the hypothesis value contradicts the estimate of more than'suraj_runs_premise'
    label = "contradiction"
elif suraj_runs_hypothesis > suraj_runs_premise:
    # the hypothesis value is greater than the premise estimate, so we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of innings played by Suraj
    # any number of innings greater than'suraj_runs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
