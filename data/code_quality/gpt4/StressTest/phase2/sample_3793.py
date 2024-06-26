bird_seed_use_premise = 20
bird_seed_use_hypothesis = 60
parakeets_premise = 20
parakeets_hypothesis = 20

# the hypothesis refers to the amount of bird seed used and the number of parakeets at Jerri's Pet Shop, mentioned in the premise
if bird_seed_use_hypothesis <= bird_seed_use_premise:
    # check if the amount of bird seed in the hypothesis contradicts the premise estimate of more than 'bird_seed_use_premise'
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of bird seed used
    # an amount of bird seed greater than 'bird_seed_use_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
