miles_per_gallon_premise = 32
miles_per_gallon_hypothesis = 82

# the hypothesis talks about the miles per gallon of Dan's car, referenced also in the premise
if miles_per_gallon_hypothesis == miles_per_gallon_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific value for the miles per gallon
    # any other value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
