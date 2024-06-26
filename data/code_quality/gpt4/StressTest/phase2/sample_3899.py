total_amount_premise = 5400
total_amount_hypothesis = 5400

# the hypothesis refers to the total amount among John, Jose & Binoy mentioned in the premise
if total_amount_hypothesis >= total_amount_premise:
    # check if the 'total_amount_hypothesis' contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
