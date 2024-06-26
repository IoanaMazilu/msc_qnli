john_minutes_premise = 30
john_minutes_hypothesis = float(30) - 1
todd_minutes_premise = 60

# the hypothesis refers to the time it takes John and Todd to rake the lawn
if john_minutes_premise <= john_minutes_hypothesis and todd_minutes_premise == todd_minutes_hypothesis:
    # check if the hypothesis values and estimates do not contradict the premise ones
    label = "neutral"
elif john_minutes_hypothesis < john_minutes_premise:
    # check if the estimate of 'john_minutes_hypothesis' contradicts the time it takes John to rake the lawn in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time it takes John and Todd to rake the lawn
    # any time less than 'john_minutes_premise' and 'todd_minutes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
