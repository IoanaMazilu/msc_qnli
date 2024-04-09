john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis talks about the percentage of the tip John paid, referenced also in the premise
if john_tip_hypothesis!= john_tip_premise:
    # check if the percentage of the tip John paid in the hypothesis contradicts the percentage of the tip John paid in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
