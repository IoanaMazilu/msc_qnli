tanya_efficiency_premise = 25
tanya_efficiency_hypothesis = 55

# the hypothesis talks about Tanya's efficiency relative to Sakshi, which is also mentioned in the premise
if tanya_efficiency_premise >= tanya_efficiency_hypothesis:
    # check if the premise's value contradicts the hypothesis that Tanya is less than 'tanya_efficiency_hypothesis'
    label = "contradiction"
else:
    # if the premise's Tanya's efficiency is less than 'tanya_efficiency_hypothesis', it cannot be directly inferred from the premise
    # thus, the relationship is neutral
    label = "neutral"

print(label)
