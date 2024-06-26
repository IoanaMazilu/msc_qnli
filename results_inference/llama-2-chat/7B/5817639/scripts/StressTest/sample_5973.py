travel_premise = 8
travel_hypothesis = 4 + 20

# the hypothesis talks about the distance and speed traveled by Jerry, referenced also in the premise
if travel_hypothesis <= travel_premise:
    # check if the hypothesis value contradicts the estimate of 'travel_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance and speed traveled by Jerry
    # any distance and speed traveled by Jerry that is consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
