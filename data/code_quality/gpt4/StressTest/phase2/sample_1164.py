distance_travelled_premise = 1/2
distance_travelled_hypothesis = 7/2

# the hypothesis talks about the distance Maria travelled during a trip, which is also referenced in the premise
if distance_travelled_hypothesis < distance_travelled_premise:
    # check if the hypothesis value contradicts the exact distance travelled in the premise
    label = "contradiction"
elif distance_travelled_hypothesis == distance_travelled_premise:
    # if the hypothesis value and the premise value are equal, we can infer entailment
    label = "entailment"
else:
    # the premise gives an exact distance for Maria's travel
    # any distance less than 'distance_travelled_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
