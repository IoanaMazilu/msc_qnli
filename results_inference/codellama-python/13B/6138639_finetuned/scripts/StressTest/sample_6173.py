tip_john_premise = 15
tip_john_hypothesis = 25

# the hypothesis talks about the tip percentage paid by John, which is also mentioned in the premise
if tip_john_hypothesis!= tip_john_premise:
    # check if the tip percentage in the hypothesis contradicts the tip percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
