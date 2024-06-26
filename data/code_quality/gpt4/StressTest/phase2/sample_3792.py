bird_seed_premise = 60
bird_seed_hypothesis = 20
parakeets_premise = 20
parakeets_hypothesis = 20

# the hypothesis refers to the number of bird seed cups and parakeets mentioned in the premise
if bird_seed_hypothesis >= bird_seed_premise:
    # check if the hypothesis contradicts the number of bird seed cups used in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
