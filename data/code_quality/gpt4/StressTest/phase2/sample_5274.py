messages_received_premise = 18
messages_received_hypothesis = 78

# the hypothesis refers to the number of messages Missy received from Laurence, mentioned in the premise
if messages_received_premise >= messages_received_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'messages_received_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the number of messages
    # number of messages in the premise is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
