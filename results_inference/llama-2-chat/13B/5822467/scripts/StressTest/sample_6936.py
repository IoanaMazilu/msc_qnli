floor_premise = 11
rate_premise = 57
floor_hypothesis = 31
rate_hypothesis = 57

# the hypothesis talks about the floor where Stalin gets on the elevator and the rate at which he rides up
if floor_hypothesis < floor_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif rate_hypothesis == rate_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise gives only an estimate for the floor where Stalin gets on the elevator
    # any floor less than or equal to 31 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
