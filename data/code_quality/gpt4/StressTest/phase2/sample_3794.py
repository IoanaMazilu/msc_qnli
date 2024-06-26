seed_usage_premise = 60
seed_usage_hypothesis = 20
days_premise = 5
days_hypothesis = 5
parakeets_premise = 20
parakeets_hypothesis = 20

# the hypothesis refers to the bird seed usage, days and parakeets number mentioned in the premise
if seed_usage_hypothesis != seed_usage_premise:
    # check if the bird seed usage in the hypothesis contradicts the bird seed usage reported in the premise
    label = "contradiction"
elif days_hypothesis != days_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise:
    # check if the number of parakeets in the hypothesis contradicts the number of parakeets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
