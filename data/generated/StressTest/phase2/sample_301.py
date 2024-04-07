# Premise: The product of the ages of Syam and Sunil is less than 540.
# Hypothesis: The product of the ages of Syam and Sunil is 240.
# Golden Label: neutral

product_age_premise = 540
product_age_hypothesis = 240

# the hypothesis refers to the product of the ages of Syam and Sunil mentioned in the premise
if product_age_hypothesis >= product_age_premise:
    # check if the product of the ages in the hypothesis contradicts the product of the ages in the premise, which is less than 540
    label = "contradiction"
elif product_age_hypothesis < product_age_premise:
    # if the product of the ages in the hypothesis is less than the product of the ages in the premise, which is less than 540, we can infer entailment
    label = "entailment"
else:
    # if the product of the ages in the hypothesis does not contradict the product of the ages in the premise, but cannot be explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)

