# define variables for the premise and hypothesis
num_passengers_premise = 6
num_passengers_hypothesis = 2

# check if the hypothesis value contradicts the premise
if num_passengers_hypothesis > num_passengers_premise:
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of combinations
    # any number of combinations greater than 'num_passengers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
