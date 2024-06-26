distance_traveled_premise = 300
distance_traveled_hypothesis = 200

# the hypothesis talks about the distance traveled on the first day of Louisa's vacation, which is also mentioned in the premise
if distance_traveled_hypothesis >= distance_traveled_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    label = "neutral"

print(label)
