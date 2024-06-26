miles_at_60mph_premise = 580
miles_at_60mph_hypothesis = 180
miles_at_40mph_premise = 120
miles_at_40mph_hypothesis = 120

# the hypothesis refers to the same two driving instances mentioned in the premise
if miles_at_60mph_hypothesis > miles_at_60mph_premise:
    # check if the number of miles driven at 60mph in the hypothesis contradicts the premise
    label = "contradiction"
elif miles_at_40mph_hypothesis != miles_at_40mph_premise:
    # check if the number of miles driven at 40mph in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
