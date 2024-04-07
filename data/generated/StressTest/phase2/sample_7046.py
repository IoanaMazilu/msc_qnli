# Premise: Raman travelled for 10 hours.
# Hypothesis: Raman travelled for less than 10 hours.
# Golden Label: contradiction

travel_time_premise = 10
travel_time_hypothesis = 10

# the hypothesis refers to the travel time of Raman mentioned in the premise
if travel_time_hypothesis >= travel_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
