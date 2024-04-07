# Premise: If Missy received less than 75 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received 25 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: neutral

messages_premise = 75
messages_hypothesis = 25

# the hypothesis talks about the number of messages Missy received from Laurence, also mentioned in the premise
if messages_hypothesis >= messages_premise:
    # check if the number of messages in the hypothesis contradicts the estimate of less than 'messages_premise'
    label = "contradiction"
elif messages_hypothesis < messages_premise:
    # the premise gives only an estimate for the number of messages
    # any number of messages less than 'messages_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

