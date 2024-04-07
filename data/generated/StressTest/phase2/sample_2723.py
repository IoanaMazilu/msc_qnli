# Premise: In one day, Juan sends Keith two times as many messages as he sends Laurence, and Laurence sends Missy 8 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith two times as many messages as he sends Laurence, and Laurence sends Missy 3 times as many messages as he receives from Juan.
# Golden Label: contradiction

ratio_messages_juan_keith_laurence_premise = 2
ratio_messages_laurence_missy_juan_premise = 8

ratio_messages_juan_keith_laurence_hypothesis = 2
ratio_messages_laurence_missy_juan_hypothesis = 3

# The hypothesis refers to the same ratios of messages sent and received as the premise
if ratio_messages_juan_keith_laurence_premise != ratio_messages_juan_keith_laurence_hypothesis:
    # Check if the ratio of messages sent by Juan to Keith and Laurence in the hypothesis contradicts the premise
    label = "contradiction"
elif ratio_messages_laurence_missy_juan_premise != ratio_messages_laurence_missy_juan_hypothesis:
    # Check if the ratio of messages sent by Laurence to Missy and received from Juan in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the ratios in the hypothesis do not contradict the ones in the premise, then we have entailment
    label = "entailment"

print(label)

