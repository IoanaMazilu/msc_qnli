# Premise: At Sandi’s Pet Shop, 25 cups of bird seed are used every 5 days to feed 15 parakeets.
# Hypothesis: At Sandi’s Pet Shop, more than 15 cups of bird seed are used every 5 days to feed 15 parakeets.
# Golden Label: entailment

bird_seed_premise = 25
bird_seed_hypothesis = 15
parakeets_premise = 15
parakeets_hypothesis = 15

# the hypothesis refers to the amount of bird seed and parakeets mentioned in the premise
if bird_seed_hypothesis >= bird_seed_premise:
    # check if the estimate of 'bird_seed_hypothesis' contradicts the number of bird seed in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

