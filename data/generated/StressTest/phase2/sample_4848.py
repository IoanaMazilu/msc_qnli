# Premise: Joe drives 180 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives less than 580 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: entailment

distance_driven_at_60mph_premise = 180
distance_driven_at_60mph_hypothesis = 580
distance_driven_at_40mph_premise = 120
distance_driven_at_40mph_hypothesis = 120

# the hypothesis refers to the distances driven at 60mph and 40mph mentioned in the premise
if distance_driven_at_60mph_premise >= distance_driven_at_60mph_hypothesis:
    # check if the estimate of 'distance_driven_at_60mph_hypothesis' contradicts the distance driven at 60mph in the premise
    label = "contradiction"
elif distance_driven_at_40mph_hypothesis != distance_driven_at_40mph_premise:
    # check if the distance driven at 40mph in the hypothesis contradicts the distance driven at 40mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

