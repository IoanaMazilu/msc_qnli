trip_home_premise = 1/2
trip_home_hypothesis = 4/2

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis!= trip_home_premise:
    # check if the duration of the trip home in the hypothesis contradicts the duration mentioned in the premise
    label = "contradiction"
else:
    # if the duration of the trip home in the hypothesis does not contradict the duration mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
