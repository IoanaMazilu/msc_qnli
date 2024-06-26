total_distance_premise = 1/2
total_distance_hypothesis = 7/2

# the hypothesis refers to the total distance traveled and the premise mentions the distance traveled
if total_distance_hypothesis <= total_distance_premise:
    # check if the estimate of 'total_distance_hypothesis' contradicts the total distance traveled in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the total distance traveled
    # any number of roses greater than 'total_distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
