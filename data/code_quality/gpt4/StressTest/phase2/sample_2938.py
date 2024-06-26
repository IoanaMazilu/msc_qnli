total_pens_purchased_premise = 42
total_pens_purchased_hypothesis = 12

# the hypothesis talks about the total number of pens Elena purchased, also mentioned in the premise
if total_pens_purchased_hypothesis >= total_pens_purchased_premise:
    # check if the number of total pens purchased in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif total_pens_purchased_hypothesis < total_pens_purchased_premise:
    # check if the number of total pens purchased in the hypothesis is less than the estimate in the premise
    label = "entailment"
else:
    # any number less than 'total_pens_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)