# Premise: If Missy received 25 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 75 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: entailment

messages_received_premise = 25
messages_received_hypothesis = 75

# the hypothesis refers to the number of messages Missy received from Laurence, as mentioned in the premise
if messages_received_premise >= messages_received_hypothesis:
    # check if the number of messages in the premise contradicts the 'less than' estimate in the hypothesis
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we have entailment, as the premise explicitly states the number of messages
    label = "entailment"

print(label)

