# Premise: Rajan travelled for 12 hours.
# Hypothesis: Rajan travelled for less than 52 hours.
# Golden Label: entailment

travel_time_premise = 12
travel_time_hypothesis = 52

# the hypothesis refers to the travelling time of Rajan mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the estimate 'travel_time_premise' contradicts the upper limit of travel time in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

