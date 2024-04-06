# Premise: Teresa jogged 25.0 kilometers at 5.0 kilometers per hour.
# Hypothesis: Teresa jogged for 4.0 hours.
# Golden Label: contradiction

distance_premise = 25.0
speed_premise = 5.0
time_hypothesis = 4.0

# the hypothesis refers to the time Teresa jogged, which can be calculated from the premise using the speed and distance
# compute the time Teresa jogged from the premise
time_premise = distance_premise / speed_premise
if time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

