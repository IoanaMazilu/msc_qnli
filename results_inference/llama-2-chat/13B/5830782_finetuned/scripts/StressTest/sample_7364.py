discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount percentage Deepa got, which is also mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
