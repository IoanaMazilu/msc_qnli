# Premise: If Missy received 18 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 18 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: contradiction

messages_missy_premise = 18
messages_missy_hypothesis = 18

# the hypothesis refers to the number of messages Missy received from Laurence
if messages_missy_hypothesis < messages_missy_premise:
    # check if the hypothesis value contradicts the number of messages reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of messages, so any number equal to or more than 'messages_missy_premise' is consistent with the premise
    # however, since the hypothesis mentions less than 'messages_missy_premise', it cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

