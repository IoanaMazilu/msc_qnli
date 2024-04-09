fish_michael_premise = 49.0
fish_ben_premise = 18.0
total_fish_hypothesis = 67.0

# the hypothesis refers to the number of fish, which are also mentioned in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_michael_premise + fish_ben_premise
if total_fish_hypothesis!= total_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
