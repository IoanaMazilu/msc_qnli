# Premise: 288 and the true discount on the same sum for the same time is Rs.
# Hypothesis: less than 588 and the true discount on the same sum for the same time is Rs.
# Golden Label: entailment

discount_premise = 288
discount_hypothesis = 588

# the hypothesis talks about the same discount mentioned in the premise
if discount_hypothesis > discount_premise:
    # check if the hypothesis value contradicts the exact value of 'discount_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, it could be entailed or neutral
    # but since we do not know the exact range of possible discounts, we cannot infer entailment
    label = "neutral"

print(label)

