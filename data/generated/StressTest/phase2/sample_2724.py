# Premise: If Missy received 40 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 50 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: entailment

messages_premise = 40
messages_hypothesis = 50

# the hypothesis refers to the number of messages received by Missy mentioned in the premise
if messages_premise >= messages_hypothesis:
    # check if the estimate of 'messages_hypothesis' contradicts the number of messages in the premise
    label = "contradiction"
elif messages_premise < messages_hypothesis:
    # check if the number of messages in the hypothesis contradicts the number of messages reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

