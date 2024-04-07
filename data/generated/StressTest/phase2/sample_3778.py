# Premise: While driving from City A to City B, Jim drives at a constant speed of less than 70 miles per hour.
# Hypothesis: While driving from City A to City B, Jim drives at a constant speed of 40 miles per hour.
# Golden Label: neutral

speed_premise = 70
speed_hypothesis = 40

# the hypothesis refers to Jim's speed, which is also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed value in the hypothesis contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

