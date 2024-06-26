total_pens_purchased_premise = 22
total_pens_purchased_hypothesis = 12

# The hypothesis refers to the total number of pens Elena purchased, which is also mentioned in the premise
if total_pens_purchased_hypothesis >= total_pens_purchased_premise:
    # Check if the total number of pens in the hypothesis contradicts the total number of pens in the premise
    label = "contradiction"
elif total_pens_purchased_hypothesis < total_pens_purchased_premise:
    # If the total number of pens in the hypothesis is less than the total number of pens in the premise, we can infer entailment
    label = "entailment"

print(label)
