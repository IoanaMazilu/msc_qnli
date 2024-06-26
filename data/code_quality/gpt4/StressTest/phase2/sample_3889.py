bird_seed_premise = 65
bird_seed_hypothesis = 35
parakeets_premise = 14
parakeets_hypothesis = 14

# the hypothesis refers to the amount of bird seed and the number of parakeets mentioned in the premise
if bird_seed_hypothesis >= bird_seed_premise:
    # check if the amount of bird seed in the hypothesis contradicts the less than estimate in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets in the premise
    label = "contradiction"
else:
    # the amount of bird seed in the hypothesis does not contradict the premise and the number of parakeets is the same in both sentences, so we can infer entailment
    label = "entailment"

print(label)
