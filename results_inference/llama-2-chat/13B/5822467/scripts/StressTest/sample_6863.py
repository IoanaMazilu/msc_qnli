hour_premise = 1
distance_premise = 45
hour_hypothesis = 1
distance_hypothesis = 85

# the hypothesis talks about the distance traveled by Johnny after Matthew, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of 'distance_premise'
    label = "contradiction"
elif distance_premise!= distance_hypothesis:
    # check if the number of kilometers traveled by Johnny in the hypothesis contradicts the number of kilometers traveled by Matthew in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance traveled by Johnny
    # any distance greater than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
