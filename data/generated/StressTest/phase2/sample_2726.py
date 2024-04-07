# Premise: If Missy received 40 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received less than 40 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: contradiction

messages_missy_premise = 40
messages_missy_hypothesis = 40

# the hypothesis refers to the number of messages Missy received from Laurence, mentioned also in the premise
if messages_missy_hypothesis >= messages_missy_premise:
    # check if the estimate of 'messages_missy_hypothesis' contradicts the number of messages in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

