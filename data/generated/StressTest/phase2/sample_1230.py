# Premise: At Amiee’s Pet Shop, 10 cups of bird seed are used every 4 days to feed 6 parakeets.
# Hypothesis: At Amiee’s Pet Shop, less than 20 cups of bird seed are used every 4 days to feed 6 parakeets.
# Golden Label: entailment

seed_cups_used_premise = 10
seed_cups_used_hypothesis = 20
parakeets_premise = 6
parakeets_hypothesis = 6
days_premise = 4
days_hypothesis = 4

# the hypothesis specifies the number of seed cups used, the number of parakeets and the number of days, all found in the premise
if seed_cups_used_hypothesis < seed_cups_used_premise or parakeets_hypothesis != parakeets_premise or days_hypothesis != days_premise:
    # check if the values in the hypothesis contradict the ones in the premise
    label = "contradiction"
elif seed_cups_used_hypothesis > seed_cups_used_premise:
    # any number of seed cups greater than 'seed_cups_used_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

