rainfall_premise = 25
rainfall_hypothesis = 25

# the hypothesis talks about the total rainfall in the first two weeks of March in Springdale, referenced in the premise
if rainfall_hypothesis != rainfall_premise:
    # check if the total rainfall amount in the hypothesis contradicts the total rainfall amount reported in the premise
    label = "contradiction"
else:
    # the amount of rainfall from the hypothesis is the same as the one from the premise, but the hypothesis states that the amount is more than the reported one
    label = "contradiction"

print(label)
