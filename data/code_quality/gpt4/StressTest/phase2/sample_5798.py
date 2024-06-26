race_distance_premise = 1400
race_distance_hypothesis = 5400

# the hypothesis refers to the race distance mentioned in the premise
if race_distance_hypothesis != race_distance_premise:
    # check if the race distance in the hypothesis contradicts the race distance reported in the premise
    label = "contradiction"
else:
    # the race distance in the premise and hypothesis are the same, hence entailment
    label = "entailment"

print(label)
