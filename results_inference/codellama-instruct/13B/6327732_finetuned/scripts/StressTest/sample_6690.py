distance_premise = 1800
distance_hypothesis = 8800

# the hypothesis refers to the total distance travelled by Rakesh, which is mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the distance travelled in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the distance travelled by Rakesh
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)