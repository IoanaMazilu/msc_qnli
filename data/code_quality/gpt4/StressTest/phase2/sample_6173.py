john_tip_premise = 15
john_tip_hypothesis = 25

# the hypothesis talks about the tip percentages paid by John and Jane, which is also referenced in the premise
if john_tip_hypothesis != john_tip_premise:
    # check if the tip percentage paid by John in the hypothesis contradicts the tip percentage paid by John in the premise
    label = "contradiction"
else:
    # if the tip percentages paid by John in the hypothesis and premise are equal, we can infer entailment
    label = "entailment"

print(label)
