# Premise: Joke is faster than Paul, Joke and Paul each walk more than 14 KM.
# Hypothesis: Joke is faster than Paul, Joke and Paul each walk 24 KM.
# Golden Label: neutral

distance_walked_premise = 14
distance_walked_hypothesis = 24

# the hypothesis refers to the distance walked by Joke and Paul mentioned in the premise
if distance_walked_hypothesis <= distance_walked_premise:
    # check if the distance walked in the hypothesis contradicts the minimum distance walked reported in the premise
    label = "contradiction"
else:
    # the premise gives only a minimum distance for the walk
    # any distance greater than 'distance_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

