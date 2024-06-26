miles_60mph_premise = 240
miles_60mph_hypothesis = 340
miles_40mph_premise = 120
miles_40mph_hypothesis = 120

# the hypothesis refers to the miles driven at 60 miles per hour and 40 miles per hour, both mentioned in the premise
if miles_60mph_hypothesis < miles_60mph_premise:
    # check if the hypothesis value contradicts the miles driven at 60 miles per hour in the premise
    label = "contradiction"
elif miles_40mph_hypothesis != miles_40mph_premise:
    # check if the miles driven at 40 miles per hour in the hypothesis contradicts the miles driven at 40 miles per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
