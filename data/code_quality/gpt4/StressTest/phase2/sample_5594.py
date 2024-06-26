fishing_time_premise = 40
fishing_time_hypothesis = 10

# the hypothesis talks about the fishing time for Mike and Bob, referenced also in the premise
if fishing_time_hypothesis != fishing_time_premise:
    # check if the fishing time in the hypothesis contradicts the fishing time reported in the premise
    label = "contradiction"
else:
    # if the fishing time in the hypothesis does not contradict the fishing time in the premise, we can infer entailment
    label = "entailment"

print(label)
