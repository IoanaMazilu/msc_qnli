discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount on the listed price of the calculator mentioned in the premise
if discount_premise <= discount_hypothesis:
    # check if the discount in the premise contradicts the estimate of more than 'discount_hypothesis'
    label = "contradiction"
else:
    # if the discount in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
