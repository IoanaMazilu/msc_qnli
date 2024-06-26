miles_walked_premise = 2
miles_walked_hypothesis = 7

# the hypothesis refers to the distance walked by Jack, as mentioned in the premise
if miles_walked_hypothesis <= miles_walked_premise:
    # check if the distance walked in the hypothesis contradicts the estimate of more than 'miles_walked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance walked
    # any distance greater than 'miles_walked_premise' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)