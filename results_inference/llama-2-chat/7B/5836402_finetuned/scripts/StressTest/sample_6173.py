john_tip_premise = 0.15
john_tip_hypothesis = 0.25
jane_tip_premise = 0.15
jane_tip_hypothesis = 0.15

# the hypothesis talks about the tip paid by John and Jane, mentioned also in the premise
if john_tip_hypothesis!= john_tip_premise:
    # check if the tip paid by John in the hypothesis contradicts the tip paid by John in the premise
    label = "contradiction"
elif jane_tip_hypothesis!= jane_tip_premise:
    # check if the tip paid by Jane in the hypothesis contradicts the tip paid by Jane in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
