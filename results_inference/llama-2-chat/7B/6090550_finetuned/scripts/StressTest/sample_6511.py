# the hypothesis talks about a product of X, Y and Z, which is also mentioned in the premise
if xy_product_premise <= 7:
    # check if the product in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the product in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
