john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis refers to the tip percentage paid by John, mentioned also in the premise
if john_tip_premise!= john_tip_hypothesis:
    # check if the tip percentage in the hypothesis contradicts the tip percentage reported in the premise
    label = "contradiction"
else:
    # if the tip percentage in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
