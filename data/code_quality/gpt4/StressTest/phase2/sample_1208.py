trip_home_premise = 0.5
trip_home_hypothesis = 0.5

# the hypothesis talks about the duration of the trip home in comparison to the trip to the beach, also mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the premise that the trip home took 'trip_home_premise' hours longer
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we infer entailment
    label = "entailment"

print(label)
