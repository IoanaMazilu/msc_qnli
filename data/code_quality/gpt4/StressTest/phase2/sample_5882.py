wheat_purchased_premise = 30
wheat_purchased_hypothesis = 50

# the hypothesis talks about the quantity of wheat purchased, referenced also in the premise
if wheat_purchased_hypothesis == wheat_purchased_premise:
    # check if the quantity of wheat purchased in the hypothesis matches the quantity of wheat purchased reported in the premise
    label = "entailment"
elif wheat_purchased_hypothesis != wheat_purchased_premise:
    # check if the quantity of wheat purchased in the hypothesis contradicts the quantity of wheat purchased reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutral
    label = "neutral"

print(label)
