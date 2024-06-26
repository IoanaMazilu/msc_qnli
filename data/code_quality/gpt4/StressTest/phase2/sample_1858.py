sugar_per_oil_premise = 32
sugar_per_oil_hypothesis = 12

# the hypothesis refers to the ratio between the amount of sugar and oil in Laura's cookie recipe
if sugar_per_oil_hypothesis >= sugar_per_oil_premise:
    # check if the hypothesis value contradicts the estimate of less than 'sugar_per_oil_premise'
    label = "contradiction"
elif sugar_per_oil_hypothesis < sugar_per_oil_premise:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
