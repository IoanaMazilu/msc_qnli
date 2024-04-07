# Premise: If Missy received 25 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received 85 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: contradiction

messages_missy_premise = 25
messages_missy_hypothesis = 85

# the hypothesis talks about the number of messages Missy received from Laurence, referenced also in the premise
if messages_missy_hypothesis != messages_missy_premise:
    # check if the number of messages in the hypothesis contradicts the number of messages reported in the premise
    label = "contradiction"
else:
    # if the number of messages in the hypothesis does not contradict the number of messages in the premise, we can infer entailment
    label = "entailment"

print(label)

