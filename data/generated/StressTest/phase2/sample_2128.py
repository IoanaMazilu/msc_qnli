# Premise: If the trip home took less than 7/2 hour longer than the trip to the beach, how many kilometers l did Carl drive each way?
# Hypothesis: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers l did Carl drive each way?
# Golden Label: neutral

trip_home_premise = 7/2
trip_home_hypothesis = 1/2

# the hypothesis talks about the duration of the trip home in comparison to the trip to the beach, mentioned also in the premise
if trip_home_hypothesis > trip_home_premise:
    # check if the hypothesis value contradicts the estimate of less than 'trip_home_premise'
    label = "contradiction"
elif trip_home_hypothesis == trip_home_premise:
    # if the hypothesis value is exactly the same as the premise value, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the duration of the trip home
    # any duration less than 'trip_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

