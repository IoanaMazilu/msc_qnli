# Premise: While driving from City A to City B, Glen drives at a constant speed of more than 10 miles per hour.
# Hypothesis: While driving from City A to City B, Glen drives at a constant speed of 40 miles per hour.
# Golden Label: neutral

speed_premise = 10
speed_hypothesis = 40

# the hypothesis refers to Glen's driving speed from City A to City B mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

