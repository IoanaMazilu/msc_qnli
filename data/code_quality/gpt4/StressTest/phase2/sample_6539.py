speed_premise = 30
speed_hypothesis = 60

# the hypothesis talks about the constant speed of Cara driving from City A to City B, which is also mentioned in the premise
if speed_hypothesis != speed_premise:
    # check if the constant speed in the hypothesis contradicts the constant speed reported in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
