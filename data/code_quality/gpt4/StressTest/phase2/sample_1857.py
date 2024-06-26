sugar_per_oil_premise = 12
sugar_per_oil_hypothesis = 32

# the hypothesis refers to the ratio of sugar to oil in Laura's cookie recipe, as mentioned in the premise
if sugar_per_oil_hypothesis < sugar_per_oil_premise:
    # check if the 'sugar_per_oil_hypothesis' contradicts the amount of sugar per oil in the premise
    label = "contradiction"
elif sugar_per_oil_hypothesis > sugar_per_oil_premise:
    # check if the 'sugar_per_oil_hypothesis' is more than the sugar per oil in the premise
    label = "neutral"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
