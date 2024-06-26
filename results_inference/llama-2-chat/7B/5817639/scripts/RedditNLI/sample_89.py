points_premise = 103
points_hypothesis = 100

# check if the number of points in the hypothesis contradicts the number of points in the premise
if points_hypothesis!= points_premise:
    label = "contradiction"
else:
    # check if the estimated number of points in the hypothesis contradicts the premise estimate of more than 100 points
    if points_hypothesis < 100:
        label = "contradiction"
    else:
        # the premise gives only an estimate for the number of points
        # any estimate of the number of points in the hypothesis greater or equal to 100 is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"

print(label)
