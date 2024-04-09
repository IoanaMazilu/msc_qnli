trip_home_premise = 1/2
trip_home_hypothesis = 3/2

# the hypothesis refers to the duration of the trip home mentioned in the premise
if trip_home_hypothesis <= trip_home_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
