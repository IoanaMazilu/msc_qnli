selling_price_premise = 12
selling_price_hypothesis = 22

# the hypothesis refers to the selling price percentage below cost, which is also mentioned in the premise
if selling_price_premise >= selling_price_hypothesis:
    # check if the selling price percentage in the hypothesis contradicts the selling price percentage reported in the premise
    label = "contradiction"
elif selling_price_premise < selling_price_hypothesis:
    # check if the selling price percentage in the premise is less than in the hypothesis
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
