temp_january_premise = 10
temp_january_hypothesis = 15

# the hypothesis gives a more precise estimate of the temperature in January
if temp_january_hypothesis <= temp_january_premise:
    # check if the hypothesis value contradicts the estimate of more than 'temp_january_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the temperature in January
    # any temperature greater than 'temp_january_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
