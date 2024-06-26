T_premise = 5/9 * (K_premise - 32)
T_hypothesis = 105

# the hypothesis refers to the temperature in Fahrenheit
if T_hypothesis <= T_premise:
    # check if the estimate of 'T_hypothesis' contradicts the temperature in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature
    # any temperature greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
