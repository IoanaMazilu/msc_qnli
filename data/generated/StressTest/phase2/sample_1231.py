# Premise: At Amiee’s Pet Shop, less than 20 cups of bird seed are used every 4 days to feed 6 parakeets.
# Hypothesis: At Amiee’s Pet Shop, 10 cups of bird seed are used every 4 days to feed 6 parakeets.
# Golden Label: neutral

bird_seed_premise = 20
bird_seed_hypothesis = 10
parakeets_premise = 6
parakeets_hypothesis = 6

# the hypothesis refers to the number of bird seed cups and parakeets mentioned in the premise
if bird_seed_hypothesis >= bird_seed_premise:
    # check if the number of bird seed cups in the hypothesis contradicts the number of bird seed cups reported in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

