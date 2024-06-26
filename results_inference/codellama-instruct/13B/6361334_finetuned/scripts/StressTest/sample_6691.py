distance_premise = 8800
distance_hypothesis = 1800

# the hypothesis refers to the distance travelled by air, which is also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance travelled by air
    # any distance less than or equal to 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
