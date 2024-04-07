# Premise: If Missy received 18 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received 58 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: contradiction

messages_missy_premise = 18
messages_missy_hypothesis = 58

# the hypothesis refers to the number of messages Missy received from Laurence mentioned in the premise
if messages_missy_hypothesis != messages_missy_premise:
    # check if the number of messages in the hypothesis contradicts the number of messages reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and the premise ones match
    label = "neutral"

print(label)

