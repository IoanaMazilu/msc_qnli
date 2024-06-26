T_premise = 5/9 * (K_premise - 32)
T_hypothesis = 20

# the hypothesis refers to the temperature in Fahrenheit
if T_hypothesis <= T_premise:
    # check if the estimate of 'T_hypothesis' contradicts the temperature in Fahrenheit in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature in Fahrenheit
    # any temperature greater than 'T_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
