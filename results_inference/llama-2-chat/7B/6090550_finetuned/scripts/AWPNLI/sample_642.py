fish_initial = 212.0
purchased_fish = 280.0
total_fish = fish_initial + purchased_fish

# the hypothesis refers to the total number of fish, which is also calculated in the premise
# compute the total number of fish in the premise
total_fish_premise = fish_initial + purchased_fish
if total_fish!= total_fish_premise:
    # check if the total number of fish in the hypothesis contradicts the total number of fish in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
