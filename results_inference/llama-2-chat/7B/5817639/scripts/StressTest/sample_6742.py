speed_premise = 20
speed_hypothesis = 30

# the hypothesis talks about the constant speed of Ed while driving from City A to City B
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the estimate of more than'speed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the constant speed
    # any constant speed greater than'speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
