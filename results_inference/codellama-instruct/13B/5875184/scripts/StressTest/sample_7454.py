T_premise = 105
T_hypothesis = 5/9 * (K_hypothesis - 32)

# the hypothesis refers to the temperature in Fahrenheit, which is less than the temperature in Celsius
if T_hypothesis <= T_premise:
    # check if the estimate of 'T_hypothesis' contradicts the temperature in Fahrenheit mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature in Celsius
    # any temperature in Fahrenheit greater than 'T_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
