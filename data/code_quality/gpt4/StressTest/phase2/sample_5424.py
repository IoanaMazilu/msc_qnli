travelled_distance_premise = 1/2
travelled_distance_hypothesis = 2/2

# The hypothesis talks about the travelled distance during Maria's car trip, also referenced in the premise
if travelled_distance_hypothesis < travelled_distance_premise:
    # Check if the hypothesis value contradicts the premise value 'travelled_distance_premise'
    label = "contradiction"
elif travelled_distance_hypothesis == travelled_distance_premise:
    # If the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
else:
    # The premise gives only an estimate for the travelled distance
    # Any travelled distance less than or equal to 'travelled_distance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
