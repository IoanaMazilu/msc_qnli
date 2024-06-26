# John, Jose and Binoy share a total amount of 6600
# The ratio of the shares is 2:4:6

total_share_premise = 6600
total_share_hypothesis = 2600

# The hypothesis refers to the total share among John, Jose and Binoy mentioned in the premise
if total_share_hypothesis >= total_share_premise:
    # Check if the estimate of 'total_share_hypothesis' contradicts the total share in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
