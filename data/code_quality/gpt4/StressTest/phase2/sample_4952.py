john_tip_percentage_premise = 15
john_tip_percentage_hypothesis = 85

# the hypothesis refers to the percentage of the tip John paid, mentioned also in the premise
if john_tip_percentage_premise != john_tip_percentage_hypothesis:
    # check if the percentage of the tip John paid in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the percentage of the tip John paid does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
