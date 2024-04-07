# Premise: While driving from City A to City B, Cara drives at a constant speed of less than 50 miles per hour.
# Hypothesis: While driving from City A to City B, Cara drives at a constant speed of 30 miles per hour.
# Golden Label: neutral

speed_premise = 50
speed_hypothesis = 30

# the hypothesis talks about the speed of driving from City A to City B, mentioned also in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the speed
    # any speed less than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

