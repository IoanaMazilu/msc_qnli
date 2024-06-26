trip_home_longer_premise = 3/2
trip_home_longer_hypothesis = 1/2

# the hypothesis refers to the time difference between the trip to the beach and the trip home, mentioned in the premise
if trip_home_longer_hypothesis >= trip_home_longer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_longer_premise'
    label = "contradiction"
elif trip_home_longer_hypothesis < trip_home_longer_premise:
    # check if the hypothesis value is less than the estimate of less than 'trip_home_longer_premise'
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
