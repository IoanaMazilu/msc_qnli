john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis refers to the tip John paid, which is also mentioned in the premise
if john_tip_hypothesis!= john_tip_premise:
    # check if the tip percentage in the hypothesis contradicts the tip percentage mentioned in the premise
    label = "contradiction"
else:
    # if the tip percentage in the hypothesis does not contradict the tip percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
