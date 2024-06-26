temperature_premise = 5/9 * (K-32)
temperature_hypothesis = 20

# the hypothesis talks about the temperature, referenced also in the premise
if temperature_hypothesis <= temperature_premise:
    # check if the hypothesis value contradicts the estimate of less than 'temperature_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature
    # any number of temperature greater than 'temperature_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
