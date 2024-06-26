rvs_destroyed_min_premise = 12
rvs_destroyed_max_premise = 15
rvs_destroyed_min_hypothesis = 12
rvs_destroyed_max_hypothesis = 15

# the hypothesis mentions the range of destroyed RVs, which is also mentioned in the premise
if rvs_destroyed_min_hypothesis != rvs_destroyed_min_premise or rvs_destroyed_max_hypothesis != rvs_destroyed_max_premise:
    # check if the minimum or maximum number of destroyed RVs in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
