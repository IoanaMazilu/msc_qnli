discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount on the listed price of a calculator mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis estimate contradicts the discount in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
