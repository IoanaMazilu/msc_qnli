trip_home_premise = 1/2
trip_home_hypothesis = 6/2

# the hypothesis talks about the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis < trip_home_premise:
    # check if the duration of the trip home in the hypothesis contradicts the duration of the trip home mentioned in the premise
    label = "contradiction"
elif trip_home_hypothesis == trip_home_premise:
    # if the duration of the trip home in the hypothesis is equal to the duration of the trip home in the premise, we can infer entailment
    label = "entailment"
else:
    # the premise gives a specific duration for the trip home
    # a duration longer than 'trip_home_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
