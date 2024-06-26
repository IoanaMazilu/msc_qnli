total_amount_premise = 4800
total_amount_hypothesis = 3800

# the hypothesis refers to the total amount shared among John, Jose & Binoy mentioned in the premise
if total_amount_hypothesis >= total_amount_premise:
    # check if the hypothesis value contradicts the total amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
