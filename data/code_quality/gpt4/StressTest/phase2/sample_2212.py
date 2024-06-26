miles_at_60mph_premise = 620
miles_at_60mph_hypothesis = 420
miles_at_40mph_premise = 120
miles_at_40mph_hypothesis = 120

# the hypothesis refers to the distance Joe drives at 60mph and 40mph, which is also mentioned in the premise
if miles_at_60mph_hypothesis >= miles_at_60mph_premise:
    # check if the distance driven at 60mph in the hypothesis contradicts the estimate of less than 'miles_at_60mph_premise' in the premise
    label = "contradiction"
elif miles_at_40mph_hypothesis != miles_at_40mph_premise:
    # check if the distance driven at 40mph in the hypothesis contradicts the distance driven at 40mph in the premise
    label = "contradiction"
else:
    # if the distances driven at 60mph and 40mph in the hypothesis do not contradict the distances in the premise, we can infer entailment
    label = "entailment"

print(label)
