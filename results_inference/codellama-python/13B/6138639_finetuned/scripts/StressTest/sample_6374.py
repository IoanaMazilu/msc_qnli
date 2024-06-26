pencils_premise = 125
pencils_hypothesis = 525

# the hypothesis talks about the number of pencils Shreehari has, referenced also in the premise
if pencils_hypothesis!= pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
