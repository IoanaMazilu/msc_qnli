walking_rate_matthew = 3
walking_rate_johnny = 4
meeting_time_matthew_johnny = 3

# the hypothesis talks about the walking rate of Matthew and Johnny
if walking_rate_matthew <= walking_rate_johnny:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif walking_rate_matthew > walking_rate_johnny:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # if the hypothesis value and the premise value are the same, it's neutral
    label = "neutral"

print(label)
