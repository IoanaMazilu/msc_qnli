shop_premise = 4
shop_hypothesis = 3
builder_from_mumbai_premise = True

# the hypothesis refers to the number of shops in the town and the builder's origin
if shop_hypothesis <= shop_premise:
    # check if the hypothesis value contradicts the estimate of'shop_premise'
    label = "contradiction"
elif not builder_from_mumbai_premise or not shop_hypothesis:
    # check if the hypothesis value contradicts the information about the builder's origin and the number of shops
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
