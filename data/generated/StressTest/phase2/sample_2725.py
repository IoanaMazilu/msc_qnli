# Premise: If Missy received less than 50 messages from Laurence, how many messages does Keith receive from Juan?
# Hypothesis: If Missy received 40 messages from Laurence, how many messages does Keith receive from Juan?
# Golden Label: neutral

messages_missy_premise = 50
messages_missy_hypothesis = 40

# the hypothesis refers to the number of messages Missy received, which is also mentioned in the premise
if messages_missy_hypothesis >= messages_missy_premise:
    # check if the number of messages in the hypothesis contradicts the premise estimate of less than 'messages_missy_premise'
    label = "contradiction"
elif messages_missy_hypothesis < messages_missy_premise:
    # if the number of messages in the hypothesis is less than 'messages_missy_premise', it can be entailed from the premise
    label = "entailment"

print(label)

