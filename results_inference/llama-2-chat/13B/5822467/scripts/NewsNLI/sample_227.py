runs_premise = 150
wickets_premise = 6

# define variables with representative names for the numerical entities in both inputs
runs_hypothesis = 150
wickets_hypothesis = 6

# extract all quantities as valid numbers (integers or floats)
runs_premise = int(runs_premise)
wickets_premise = int(wickets_premise)
runs_hypothesis = int(runs_hypothesis)
wickets_hypothesis = int(wickets_hypothesis)

# compare the variables
if runs_hypothesis == runs_premise:
    # the hypothesis mentions the same number of runs as the premise, so there is no contradiction
    label = "neutral"
elif runs_hypothesis!= runs_premise:
    # the hypothesis mentions a different number of runs than the premise, so there is a contradiction
    label = "contradiction"
elif wickets_hypothesis!= wickets_premise:
    # the hypothesis mentions a different number of wickets than the premise, so there is a contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
