distance_travelled_premise = 8800
distance_travelled_hypothesis = 1800

# the hypothesis refers to the distance travelled by Rakesh, which is also mentioned in the premise
if distance_travelled_hypothesis >= distance_travelled_premise:
    # check if the distance travelled in the hypothesis contradicts the estimate of less than 'distance_travelled_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled
    # any distance less than 'distance_travelled_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
