purchase_kg_premise = 30
purchase_kg_hypothesis = 40

# the hypothesis refers to the amount of wheat purchased by Arun, which is also mentioned in the premise
if purchase_kg_hypothesis >= purchase_kg_premise:
    # check if the hypothesis value contradicts the amount of wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the amount of wheat purchased in the premise, we can infer entailment
    label = "entailment"

print(label)
