# define the variables for the premise and hypothesis
less_than_8_premise = 8
less_than_8_hypothesis = 4

# the hypothesis refers to the number of less than 'less_than_8_hypothesis' mentioned in the premise
if less_than_8_hypothesis >= less_than_8_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_8_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number
    # any number less than 'less_than_8_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)