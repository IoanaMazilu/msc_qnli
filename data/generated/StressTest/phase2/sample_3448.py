# Premise: Ganesh covers the distance from X to Y at an average speed of more than 50 Km/hr.
# Hypothesis: Ganesh covers the distance from X to Y at an average speed of 60 Km/hr.
# Golden Label: neutral

speed_premise = 50
speed_hypothesis = 60

# the hypothesis talks about the average speed of Ganesh traveling from X to Y, referenced also in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed
    # any speed greater than 'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

