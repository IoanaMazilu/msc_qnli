# Premise: Heather bicycled 40.0 kilometers at 8.0 kilometers per hour.
# Hypothesis: Heather bicycled for 5.0 hours.
# Golden Label: entailment

distance_premise = 40.0
speed_premise = 8.0
time_hypothesis = 5.0

# the hypothesis refers to the time Heather spent bicycling, which can be deduced from the premise
# compute the time Heather spent bicycling in the premise
time_premise = distance_premise / speed_premise
if time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

