total_share_premise = 4800
total_share_hypothesis = 3800

# the hypothesis refers to the total share among John, Jose & Binoy mentioned in the premise
if total_share_hypothesis >= total_share_premise:
    # check if the estimate of 'total_share_hypothesis' contradicts the total share in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
