# Premise: Jack and Christina are standing more than 260 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 360 feet apart on a level surface.
# Golden Label: neutral

distance_apart_premise = 260
distance_apart_hypothesis = 360

# the hypothesis refers to the distance between Jack and Christina mentioned in the premise
if distance_apart_hypothesis <= distance_apart_premise:
    # check if the hypothesis value contradicts the estimate of more than 'distance_apart_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance between Jack and Christina
    # any distance greater than 'distance_apart_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

