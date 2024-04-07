# Premise: Jack and Christina are standing less than 440 feet apart on a level surface.
# Hypothesis: Jack and Christina are standing 240 feet apart on a level surface.
# Golden Label: neutral

distance_premise = 440
distance_hypothesis = 240

# the hypothesis talks about the distance between Jack and Christina, also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

