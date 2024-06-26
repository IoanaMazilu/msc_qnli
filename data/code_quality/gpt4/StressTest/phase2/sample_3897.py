total_amount_premise = 5400
total_amount_hypothesis = 3400

# the hypothesis refers to the same total amount of money distributed among John, Jose & Binoy, which is mentioned in the premise
if total_amount_hypothesis >= total_amount_premise:
    # check if the estimate of 'total_amount_hypothesis' contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
