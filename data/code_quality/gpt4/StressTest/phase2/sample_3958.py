distance_to_walt_premise = 18
distance_to_walt_hypothesis = 48

# The hypothesis talks about the distance Lionel walked to Walt's house, which is also mentioned in the premise
if distance_to_walt_hypothesis <= distance_to_walt_premise:
    # Check if the distance in the hypothesis contradicts the estimate of more than 'distance_to_walt_premise' miles
    label = "contradiction"
else:
    # The premise gives only an estimate for the distance
    # Any distance greater than 'distance_to_walt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
