# Premise: Every Sunday, Giri jogs 3 miles.
# Hypothesis: Every Sunday, Giri jogs more than 1 miles.
# Golden Label: entailment

jogging_distance_premise = 3
jogging_distance_hypothesis = 1

# the hypothesis refers to the distance jogged by Giri, which is also mentioned in the premise
if jogging_distance_premise <= jogging_distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance mentioned in the hypothesis is less than the distance mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

