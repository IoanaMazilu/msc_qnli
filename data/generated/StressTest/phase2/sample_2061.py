# Premise: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 5 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy less than 6 times as many messages as he receives from Juan.
# Golden Label: entailment

juan_keith_premise = 3
juan_laurence_premise = 1
laurence_missy_premise = 5 * juan_laurence_premise

juan_keith_hypothesis = 3
juan_laurence_hypothesis = 1
laurence_missy_hypothesis = 6 * juan_laurence_hypothesis

# the hypothesis refers to the number of messages sent and received by Juan, Keith, Laurence and Missy, mentioned also in the premise
if juan_keith_premise != juan_keith_hypothesis or juan_laurence_premise != juan_laurence_hypothesis:
    # check if the number of messages sent by Juan in the hypothesis contradicts the number of messages sent by Juan in the premise
    label = "contradiction"
elif laurence_missy_hypothesis <= laurence_missy_premise:
    # check if the number of messages sent by Laurence in the hypothesis contradicts the number of messages sent by Laurence in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

