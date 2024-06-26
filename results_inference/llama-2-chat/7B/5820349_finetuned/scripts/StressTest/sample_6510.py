xy_product_premise = 7
xy_product_hypothesis = 5

# the hypothesis refers to the product of X, Y and Z mentioned in the premise
if xy_product_premise <= xy_product_hypothesis:
    # check if the estimate of 'xy_product_hypothesis' contradicts the number of XYZ in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
