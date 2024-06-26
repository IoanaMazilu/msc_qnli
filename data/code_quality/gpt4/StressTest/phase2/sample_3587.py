bird_seed_premise = 25
bird_seed_hypothesis = 25
parakeets_premise = 15
parakeets_hypothesis = 15

# the hypothesis refers to the same number of parakeets and bird seed consumption per 5 days as the premise
if bird_seed_hypothesis >= bird_seed_premise:
    # check if the hypothesis estimate contradicts the number of bird seed cups used in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
