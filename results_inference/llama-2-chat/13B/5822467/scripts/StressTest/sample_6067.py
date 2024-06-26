less_than_5_shops_premise = 5
builder_from_mumbai_premise = "Mumbai"
four_to_five_shops_hypothesis = 4

# the hypothesis refers to the number of shops in the town and the builder's location
if four_to_five_shops_hypothesis <= less_than_5_shops_premise:
    # check if the hypothesis value contradicts the estimate of less than 5 shops in the premise
    label = "contradiction"
elif builder_from_mumbai_hypothesis!= builder_from_mumbai_premise:
    # check if the builder's location in the hypothesis contradicts the location reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
