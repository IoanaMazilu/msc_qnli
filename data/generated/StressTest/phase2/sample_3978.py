# Premise: If the trip home took 1/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Hypothesis: If the trip home took less than 6/2 hour longer than the trip to the beach, how many kilometers k did Carl drive each way?
# Golden Label: entailment

trip_home_premise = 1/2
trip_home_hypothesis = 6/2

# the hypothesis talks about the duration of the trip home, also mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis estimate contradicts the premise duration
    label = "contradiction"
elif trip_home_hypothesis < trip_home_premise:
    # check if the hypothesis duration contradicts the premise estimate
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

