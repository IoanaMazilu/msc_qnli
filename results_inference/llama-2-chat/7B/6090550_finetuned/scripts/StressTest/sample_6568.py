trip_home_premise = 7/2
trip_home_hypothesis = 1/2

# the hypothesis refers to the duration of the trip home, which is also mentioned in the premise
if trip_home_hypothesis >= trip_home_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif trip_home_hypothesis < trip_home_premise:
    # if the hypothesis value is less than the premise, it entails the hypothesis
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise, it is neutral
    label = "neutral"

print(label)
