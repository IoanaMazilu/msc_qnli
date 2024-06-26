messages_received_missy_premise = 18
messages_received_missy_hypothesis = 78

# the hypothesis talks about the number of messages Missy received from Laurence, referenced also in the premise
if messages_received_missy_hypothesis != messages_received_missy_premise:
    # the number of messages received by Missy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are identical
    label = "entailment"

print(label)
