travel_premise = 7
travel_hypothesis = float("more than 7")

# the hypothesis talks about the time taken for the journey, which is also mentioned in the premise
if travel_hypothesis >= travel_premise:
    # check if the hypothesis value contradicts the estimate of 7 hours given in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the time taken, but the hypothesis value cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
