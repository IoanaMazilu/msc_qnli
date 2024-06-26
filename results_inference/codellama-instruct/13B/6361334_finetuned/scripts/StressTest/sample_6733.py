# define variables for the premise and hypothesis
premise_distance = 3
hypothesis_distance = 2

# check if the hypothesis distance contradicts the premise distance
if hypothesis_distance >= premise_distance:
    label = "contradiction"
else:
    # the hypothesis distance is less than the premise distance
    # any number of routes greater than 1 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
