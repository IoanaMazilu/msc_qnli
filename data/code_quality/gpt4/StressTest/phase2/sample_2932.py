distance_to_walt_premise = 68
distance_to_walt_hypothesis = 48

# the hypothesis talks about the distance Lionel walked, referenced also in the premise
if distance_to_walt_hypothesis > distance_to_walt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'distance_to_walt_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the distance Lionel walked
    # any distance less than 'distance_to_walt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
