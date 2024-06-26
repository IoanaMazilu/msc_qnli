john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis refers to the percentage of the tip John paid over the dish's price
if john_tip_premise >= john_tip_hypothesis:
    # check if the percentage of 'john_tip_hypothesis' contradicts the percentage of tip John paid in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
