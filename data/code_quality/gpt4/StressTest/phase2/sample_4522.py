messages_premise = 68
messages_hypothesis = 18

# the hypothesis references the number of messages received by Missy from Laurence, which is also mentioned in the premise
if messages_hypothesis >= messages_premise:
    # check if the hypothesis value contradicts the estimate of less than 'messages_premise'
    label = "contradiction"
elif messages_hypothesis < messages_premise:
    # if the hypothesis value is less than 'messages_premise', it is consistent with the premise, but we cannot explicitly entail it from the premise
    label = "neutral"

print(label)
