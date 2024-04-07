# Premise: Jack and Christina are standing less than 470 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 270 feet apart on a level surface.
# Golden Label: neutral

distance_premise = 470
distance_hypothesis = 270

# the hypothesis refers to the distance between Jack and Christina, which is also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # check if the hypothesis value exactly equals 'distance_premise'
    # this would contradict the premise's claim of Jack and Christina being less than 'distance_premise' apart
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

