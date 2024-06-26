tank_1_premise = 212.0
tank_2_premise = 68.0
tank_1_hypothesis = 144.0

# the hypothesis refers to the number of fish in the first tank, which are also mentioned in the premise
# compute the total number of fish in the first tank
total_fish_premise = tank_1_premise + tank_2_premise
if total_fish_hypothesis!= total_fish_premise:
    # check if the number of fish in the hypothesis contradicts the number of fish from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
