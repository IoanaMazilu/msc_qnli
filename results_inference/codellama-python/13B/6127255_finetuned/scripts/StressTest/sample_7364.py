discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount percentage on the calculator's listed price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # if the discount percentage in the hypothesis is less than the discount percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
