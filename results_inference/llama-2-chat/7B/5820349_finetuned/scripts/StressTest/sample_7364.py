discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount percentage on the listed price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
