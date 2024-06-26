bird_seed_premise = 10
bird_seed_hypothesis = 70
parakeets_premise = 6
parakeets_hypothesis = 6
days_premise = 4
days_hypothesis = 4

# the hypothesis refers to the number of cups of bird seed used and parakeets mentioned in the premise
if bird_seed_hypothesis != bird_seed_premise:
    # check if the number of cups of bird seed in the hypothesis contradicts the number of cups reported in the premise
    label = "contradiction"
elif parakeets_hypothesis != parakeets_premise or days_hypothesis != days_premise:
    # check if the number of parakeets or days in the hypothesis contradicts the numbers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment or neutrality
    label = "entailment"

print(label)
