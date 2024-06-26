speed_premise = 50
speed_hypothesis = 30

# the hypothesis refers to the speed of Cara's drive from City A to City B, also mentioned in the premise
if speed_hypothesis >= speed_premise:
    # check if the speed in the hypothesis contradicts the estimate of less than'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed
    # any speed less than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
