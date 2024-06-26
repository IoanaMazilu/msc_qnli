# compute the total number of roses in the premise
total_roses_premise = roses_premise + roses_sold_premise + roses_picked_premise

# check if the hypothesis value is within the range of the total number of roses in the premise
if roses_hypothesis >= total_roses_premise:
    # if the hypothesis value is greater than or equal to the total number of roses in the premise, we can infer entailment
    label = "entailment"
elif roses_hypothesis < total_roses_premise:
    # if the hypothesis value is less than the total number of roses in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is equal to the total number of roses in the premise, we can infer neutrality
    label = "neutral"

print(label)
