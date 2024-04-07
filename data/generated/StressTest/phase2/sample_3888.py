# Premise: At Pete’s Pet Shop, 35 cups of bird seed are used every 5 days to feed 14 parakeets.
# Hypothesis: At Pete’s Pet Shop, less than 65 cups of bird seed are used every 5 days to feed 14 parakeets.
# Golden Label: entailment

bird_seed_premise = 35
bird_seed_hypothesis = 65
parakeets_premise = 14
parakeets_hypothesis = 14

# the hypothesis refers to the number of bird seed cups and parakeets mentioned in the premise
if bird_seed_hypothesis <= bird_seed_premise:
    # check if the value of 'bird_seed_hypothesis' contradicts the number of bird seed cups in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

