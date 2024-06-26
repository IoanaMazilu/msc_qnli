messages_premise = 38
messages_hypothesis = 18

# the hypothesis talks about the number of messages Missy received from Laurence, which is also referenced in the premise
if messages_hypothesis >= messages_premise:
    # check if the hypothesis value contradicts the estimate of less than 'messages_premise'
    label = "contradiction"
elif messages_hypothesis < messages_premise:
    # the premise gives an estimate for the number of messages
    # the hypothesis number is less than 'messages_premise', hence consistent with the premise
    # but we cannot for sure say it is an entailment
    label = "neutral"

print(label)
