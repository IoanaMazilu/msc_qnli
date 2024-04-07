# Premise: If Missy received 18 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 38 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: entailment

messages_to_missy_premise = 18
messages_to_missy_hypothesis = 38

# the hypothesis refers to the number of messages Missy received from Laurence mentioned in the premise
if messages_to_missy_premise >= messages_to_missy_hypothesis:
    # check if the number of messages to Missy in the premise contradicts the estimate of less than 'messages_to_missy_hypothesis'
    label = "contradiction"
elif messages_to_missy_premise < messages_to_missy_hypothesis:
    # if the number of messages Missy received doesn't contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

