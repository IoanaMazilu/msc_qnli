average_speed_premise = 4
average_speed_hypothesis = 1

# the hypothesis refers to the ratio of distances between A to B and B to C
if average_speed_hypothesis <= average_speed_premise:
    # check if the estimate of 'average_speed_hypothesis' contradicts the number of cookie sales in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of roses
    # any number of roses greater than 'roses_vase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
