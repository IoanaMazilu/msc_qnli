# Premise: While driving from City A to City B, Cara drives at a constant speed of more than 10 miles per hour.
# Hypothesis: While driving from City A to City B, Cara drives at a constant speed of 30 miles per hour.
# Golden Label: neutral

speed_premise = 10
speed_hypothesis = 30

# the hypothesis refers to the driving speed from City A to City B, also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

