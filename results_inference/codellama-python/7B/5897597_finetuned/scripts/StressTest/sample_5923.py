trip_home_premise = 3/2
trip_home_hypothesis = 1/2

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the trip home
    # any duration less than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
