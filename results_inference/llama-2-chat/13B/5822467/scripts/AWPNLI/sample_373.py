dimes_premise = 7.0
dimes_given_dad_premise = 8.0
dimes_given_mom_premise = 4.0
dimes_hypothesis = 5.0

# compute the total number of dimes in the premise
total_dimes_premise = dimes_premise + dimes_given_dad_premise + dimes_given_mom_premise

if dimes_hypothesis > total_dimes_premise:
    # the hypothesis implies that Melanie has more dimes than the total number of dimes in the premise, so there is a contradiction
    label = "contradiction"
elif dimes_hypothesis < total_dimes_premise:
    # the hypothesis implies that Melanie has fewer dimes than the total number of dimes in the premise, so there is no entailment
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
