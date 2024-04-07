# Premise: In one day, Juan sends Keith two times as many messages as he sends Laurence, and Laurence sends Missy 8 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith two times as many messages as he sends Laurence, and Laurence sends Missy more than 7 times as many messages as he receives from Juan.
# Golden Label: entailment

juan_keith_laurence_ratio_premise = 2
juan_keith_laurence_ratio_hypothesis = 2
laurence_missy_juan_ratio_premise = 8
laurence_missy_juan_ratio_hypothesis = 7

# The hypothesis talks about the ratio of messages sent between Juan, Keith, Laurence and Missy, which is also referenced in the premise
if juan_keith_laurence_ratio_hypothesis != juan_keith_laurence_ratio_premise:
    # Check if the ratio of messages between Juan, Keith and Laurence in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif laurence_missy_juan_ratio_hypothesis >= laurence_missy_juan_ratio_premise:
    # Check if the ratio of messages between Laurence, Missy and Juan in the hypothesis contradicts the ratio mentioned in the premise
    label = "contradiction"
elif juan_keith_laurence_ratio_hypothesis == juan_keith_laurence_ratio_premise and laurence_missy_juan_ratio_hypothesis < laurence_missy_juan_ratio_premise:
    # If the ratio of messages between Juan, Keith and Laurence in the hypothesis matches exactly with the premise and the ratio of messages between Laurence, Missy and Juan in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, but also cannot be fully entailed from them, we have a neutral relation
    label = "neutral"

print(label)

