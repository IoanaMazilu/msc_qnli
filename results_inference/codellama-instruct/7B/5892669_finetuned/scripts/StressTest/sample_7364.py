discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount on the listed price of the calculator bought by Deepa, mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
