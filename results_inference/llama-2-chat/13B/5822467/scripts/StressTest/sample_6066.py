shops_premise = 4
shops_hypothesis = 5
builder_from_mumbai_premise = True

# the hypothesis refers to the number of shops and the builder's location
if shops_hypothesis <= shops_premise:
    # check if the hypothesis value contradicts the estimate of'shops_premise'
    label = "contradiction"
elif not builder_from_mumbai_premise or not builder_from_mumbai_hypothesis:
    # check if the builder's location in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
