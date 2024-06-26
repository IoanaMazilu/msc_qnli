distance_premise = 60
distance_hypothesis = 40

# the hypothesis talks about the distance from Marathon to Athens, referenced also in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the premise of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
