# Premise: At Sandi’s Pet Shop, more than 15 cups of bird seed are used every 5 days to feed 15 parakeets.
# Hypothesis: At Sandi’s Pet Shop, 25 cups of bird seed are used every 5 days to feed 15 parakeets.
# Golden Label: neutral

bird_seed_premise = 15
bird_seed_hypothesis = 25
parakeets_premise = 15
parakeets_hypothesis = 15

# The hypothesis refers to the bird seed consumption and number of parakeets mentioned in the premise
if bird_seed_hypothesis <= bird_seed_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'bird_seed_premise'
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # Check if the number of parakeets in the hypothesis contradicts the number of parakeets mentioned in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the bird seed consumption
    # Any number of bird seed cups greater than 'bird_seed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

