fish_premise = 261.0
fishbowls_premise = 23.0
hypothesis_fishbowls = 12.5

# compute the total number of fish in the premise
total_fish_premise = fish_premise * fishbowls_premise

# check if the number of fishbowls in the hypothesis contradicts the number of fish in the premise
if hypothesis_fishbowls!= total_fish_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
