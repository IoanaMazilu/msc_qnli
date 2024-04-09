amount_premise = float(7)
amount_hypothesis = float(3)

# the hypothesis refers to the amount of money given back to parents each month, mentioned in the premise
if amount_hypothesis <= amount_premise:
    # check if the estimate of 'amount_hypothesis' contradicts the amount of money given back in the premise
    label = "contradiction"
elif amount_hypothesis / amount_premise > 0.5:
    # check if the ratio of the amount of money given back in the hypothesis to the amount given back in the premise is greater than 0.5, which means the hypothesis implies more than 50% of the amount given back in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
