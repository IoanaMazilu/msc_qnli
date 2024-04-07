# Premise: Flora leaves City A more than 1 hours after Ed.
# Hypothesis: Flora leaves City A 2 hours after Ed.
# Golden Label: neutral

flora_departure_premise = 1
flora_departure_hypothesis = 2

# the hypothesis refers to the time Flora leaves City A, mentioned also in the premise
if flora_departure_hypothesis <= flora_departure_premise:
    # check if the time in the hypothesis contradicts the estimate of more than 'flora_departure_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'flora_departure_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

