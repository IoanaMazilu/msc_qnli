distance_air_premise = 8800
distance_air_hypothesis = 1800

# the hypothesis refers to the distance travelled by air, which is also mentioned in the premise
if distance_air_hypothesis >= distance_air_premise:
    # check if the distance travelled by air in the hypothesis contradicts the premise
    label = "contradiction"
elif distance_air_hypothesis < distance_air_premise:
    # if the distance travelled by air in the hypothesis is less than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
