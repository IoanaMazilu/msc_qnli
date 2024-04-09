share_premise = 200
share_hypothesis = 400

# the hypothesis talks about the difference between Mani and Rani's share, which is also mentioned in the premise
if share_hypothesis - share_premise <= 0:
    # check if the hypothesis value contradicts the estimate of the difference between Mani and Rani's share in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the difference between Mani and Rani's share
    # any difference greater than 0 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
