# Premise: The product of the ages of Syam and Sunil is 240.
# Hypothesis: The product of the ages of Syam and Sunil is more than 240.
# Golden Label: contradiction

product_ages_premise = 240
product_ages_hypothesis = 240

# the hypothesis refers to the product of the ages of Syam and Sunil mentioned in the premise
if product_ages_hypothesis > product_ages_premise:
    # the hypothesis asserts that the product of the ages is more than the actual product stated in the premise
    label = "contradiction"
elif product_ages_hypothesis < product_ages_premise:
    # the hypothesis asserts that the product of the ages is less than stated in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

