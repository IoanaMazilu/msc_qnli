# Premise: If Missy received 18 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 68 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: entailment

messages_received_premise = 18
messages_received_hypothesis = 68

# the hypothesis refers to the number of messages Missy received from Laurence as mentioned in the premise
if messages_received_hypothesis <= messages_received_premise:
    # check if the estimate of 'messages_received_hypothesis' contradicts the number of messages received in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

