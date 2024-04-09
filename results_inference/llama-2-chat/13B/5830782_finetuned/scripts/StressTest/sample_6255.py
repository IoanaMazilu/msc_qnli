discount_premise = 20
discount_hypothesis = 30

# the hypothesis refers to the discount percentage Saren negotiated, mentioned in the premise
if discount_premise >= discount_hypothesis:
    # check if the discount percentage in the premise contradicts the estimate of less than 'discount_hypothesis'
    label = "contradiction"
else:
    # if the discount percentage in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
