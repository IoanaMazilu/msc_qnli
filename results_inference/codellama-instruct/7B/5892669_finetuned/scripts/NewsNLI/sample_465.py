outstanding_fines_min_premise = 10000
outstanding_fines_max_premise = 29000000
outstanding_fines_max_hypothesis = 4500000

# the hypothesis mentions the maximum amount of outstanding fines, which is also referenced in the premise
if outstanding_fines_max_hypothesis > outstanding_fines_max_premise:
    # check if the maximum amount of outstanding fines in the hypothesis contradicts the maximum amount reported in the premise
    label = "contradiction"
else:
    # if the maximum amount of outstanding fines in the hypothesis does not contradict the maximum amount in the premise, we can infer entailment
    label = "entailment"

print(label)
