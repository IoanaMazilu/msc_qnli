floors_premise = 51
floors_hypothesis = 61
rate_premise = 63

# the hypothesis refers to the floor where Albert gets on the elevator and the rate at which the elevator descends
if floors_hypothesis > floors_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif floors_hypothesis == floors_premise and rate_premise == rate_hypothesis:
    # check if the rate at which the elevator descends is consistent with both the premise and the hypothesis
    label = "neutral"
else:
    # the premise gives only an estimate for the floor where Albert gets on the elevator
    # any floor less than or equal to 61 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
