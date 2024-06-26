discount_premise = 0.3
discount_hypothesis = 0.10

# the hypothesis refers to the discount on the listed price of a calculator, mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
