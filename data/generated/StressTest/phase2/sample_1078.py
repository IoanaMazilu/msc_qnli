# Premise: Every Sunday, Giri jogs more than 1 miles.
# Hypothesis: Every Sunday, Giri jogs 3 miles.
# Golden Label: neutral

jogging_distance_premise = 1
jogging_distance_hypothesis = 3

# the hypothesis refers to the distance Giri jogs on Sundays, also mentioned in the premise
if jogging_distance_hypothesis <= jogging_distance_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jogging_distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the jogging distance
    # any distance greater than 'jogging_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

