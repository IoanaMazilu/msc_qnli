# Premise: Raman travelled for 10 hours.
# Hypothesis: Raman travelled for less than 20 hours.
# Golden Label: entailment

travel_time_premise = 10
travel_time_hypothesis = 20

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_premise >= travel_time_hypothesis:
    # check if the estimate of 'travel_time_hypothesis' contradicts the travel time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
