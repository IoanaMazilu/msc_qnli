distance_covered_premise = 500
distance_covered_hypothesis = 500
speed_sandy = 15

# the hypothesis talks about the distance Sandy covers and the speed at which Sandy runs, referenced also in the premise
if distance_covered_hypothesis <= distance_covered_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise talks about a specific distance while the hypothesis talks about a distance greater than the one mentioned in the premise
    # the premise cannot explicitly entail the hypothesis
    label = "neutral"

print(label)
