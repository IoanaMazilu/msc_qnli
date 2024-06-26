miles_at_60mph_premise = 360
miles_at_60mph_hypothesis = 460
miles_at_40mph_premise = 120
miles_at_40mph_hypothesis = 120

# the hypothesis talks about the distance driven at 60mph and 40mph, both referenced in the premise
if miles_at_60mph_hypothesis >= miles_at_60mph_premise:
    # check if the hypothesis estimate contradicts the distance driven at 60mph in the premise
    label = "contradiction"
elif miles_at_40mph_hypothesis != miles_at_40mph_premise:
    # check if the distance driven at 40mph in the hypothesis contradicts the distance driven at 40mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
