saved_dollars_premise = 21
allowance_dollars_premise = 15
gamble_multiplier = 6
total_dollars_hypothesis = 216.0

# the hypothesis refers to the total amount of dollars, which can be computed from the premise
# compute the total dollars after gambling in the premise
total_dollars_premise = (saved_dollars_premise + allowance_dollars_premise) * gamble_multiplier
if total_dollars_hypothesis != total_dollars_premise:
    # check if the total dollars in the hypothesis contradicts the total dollars from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
