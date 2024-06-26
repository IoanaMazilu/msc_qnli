# defining variables for the premise and hypothesis
xy_product_premise = 7
xy_product_hypothesis = 3

# the hypothesis refers to a product of X, Y and Z, also mentioned in the premise
if xy_product_premise!= xy_product_hypothesis:
    # check if the product in the hypothesis contradicts the product in the premise
    label = "contradiction"
else:
    # if the product in the hypothesis does not contradict the product in the premise, we can infer entailment
    label = "entailment"

print(label)
