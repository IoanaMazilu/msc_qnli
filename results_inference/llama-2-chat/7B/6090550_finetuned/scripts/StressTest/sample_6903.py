total_amount_paid_premise = 160
total_amount_paid_hypothesis = 360

# the hypothesis refers to the total amount paid for renting the tool, which is also mentioned in the premise
if total_amount_paid_hypothesis < total_amount_paid_premise:
    # check if the amount in the hypothesis contradicts the amount in the premise
    label = "contradiction"
elif total_amount_paid_hypothesis == total_amount_paid_premise:
    # check if the amount in the hypothesis matches the amount in the premise
    label = "entailment"
else:
    # if the hypothesis values do not contradict or match the premise ones, we can infer neutrality
    label = "neutral"

print(label)
