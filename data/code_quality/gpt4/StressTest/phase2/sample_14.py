speed_premise = 85
speed_hypothesis = 85

# the hypothesis talks about the speed at which John drives, referenced also in the premise
if speed_hypothesis > speed_premise:
    # check if the hypothesis value contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis speed does not contradict the premise speed, we can infer entailment
    label = "entailment"

print(label)
