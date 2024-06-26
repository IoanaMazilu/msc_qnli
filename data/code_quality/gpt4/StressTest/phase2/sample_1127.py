supermarkets_difference_premise = 10
supermarkets_difference_hypothesis = 10

# the hypothesis refers to the difference in the number of FGH supermarkets between the US and Canada mentioned in the premise
if supermarkets_difference_hypothesis > supermarkets_difference_premise:
    # check if the hypothesis value contradicts the number of 'supermarkets_difference_premise'
    label = "contradiction"
elif supermarkets_difference_hypothesis < supermarkets_difference_premise:
    # check if the hypothesis value is less than 'supermarkets_difference_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
