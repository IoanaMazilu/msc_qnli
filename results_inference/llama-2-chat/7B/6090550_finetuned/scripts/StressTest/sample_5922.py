# defining the variables
trip_home_premise = 0.5
trip_home_hypothesis = 3.5

# the hypothesis refers to the time difference between the trip to the beach and the trip home
if trip_home_premise >= trip_home_hypothesis:
    # check if the time difference in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the time difference in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
