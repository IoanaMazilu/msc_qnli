fish_premise = 261.0
fish_bowls_premise = 23.0
fish_hypothesis = 12.5

# the hypothesis talks about the number of fishbowls, which is also mentioned in the premise
# compute the total number of fishbowls in the premise
total_fish_bowls_premise = fish_bowls_premise + fish_hypothesis

# check if the number of fishbowls in the hypothesis contradicts the number of fishbowls from the premise
if total_fish_bowls_hypothesis!= total_fish_bowls_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
