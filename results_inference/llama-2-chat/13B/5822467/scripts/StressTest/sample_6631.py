distance_premise = 800
distance_hypothesis = 500
speed_premise = 15

# the hypothesis talks about the distance covered by Sandy, referenced also in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the distance covered
    # any distance less than or equal to 500 meters is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
