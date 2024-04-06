# Premise: Lawrence walked 4.0 kilometers at 3.0 kilometers per hour.
# Hypothesis: Lawrence walked for 1.333333 hours.
# Golden Label: entailment

distance_walked_premise = 4.0 
speed_premise = 3.0
time_walked_hypothesis = 1.333333 

# the hypothesis refers to the time walked, which can be calculated from the premise
# compute the time walked in the premise
time_walked_premise = distance_walked_premise / speed_premise
if abs(time_walked_hypothesis - time_walked_premise) > 0.000001: 
    # check if the time walked in the hypothesis contradicts the time walked calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

