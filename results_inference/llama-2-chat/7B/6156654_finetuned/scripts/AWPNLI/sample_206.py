fishbowls = 261.0
fish_per_fishbowl = 23.0
total_fish = fishbowls * fish_per_fishbowl

# the hypothesis refers to the total number of fish, which can be calculated from the premise
# the hypothesis number is larger than the total number of fish in the premise
if total_fish!= 6003.0:
    # check if the total number of fish in the hypothesis contradicts the total number of fish in the premise
    label = "contradiction"
else:
    # if the hypothesis number matches the total number of fish in the premise, we can infer entailment
    label = "entailment"

print(label)
