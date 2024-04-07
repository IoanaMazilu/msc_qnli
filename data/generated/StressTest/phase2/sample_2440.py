# Premise: Sourav walks less than 80 meters towards North.
# Hypothesis: Sourav walks 20 meters towards North.
# Golden Label: neutral

walk_distance_premise = 80
walk_distance_hypothesis = 20

# the hypothesis refers to the distance Sourav walks towards North mentioned in the premise
if walk_distance_hypothesis >= walk_distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'walk_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the walking distance
    # any distance less than 'walk_distance_premise' is consistent with the premise
    # the exact value from the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)

