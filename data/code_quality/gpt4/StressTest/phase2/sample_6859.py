miles_walked_premise = 3
miles_walked_hypothesis = 4

# the hypothesis refers to the distance walked by Jack mentioned in the premise
if miles_walked_hypothesis <= miles_walked_premise:
    # check if the distance in the hypothesis contradicts the premise that states Jack walked more than 'miles_walked_premise' miles
    label = "contradiction"
else:
    # the premise gives only an estimation for the distance walked
    # any distance greater than 'miles_walked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
