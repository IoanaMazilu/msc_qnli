# Premise: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 5 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 6 times as many messages as he receives from Juan.
# Golden Label: contradiction

juan_keith_premise = 3
juan_laurence_premise = 1
laurence_missy_premise = 5 * juan_laurence_premise

juan_keith_hypothesis = 3
juan_laurence_hypothesis = 1
laurence_missy_hypothesis = 6 * juan_laurence_hypothesis

# both the premise and the hypothesis refer to the number of messages that Juan sends Keith and Laurence and the number of messages that Laurence sends Missy
if juan_keith_hypothesis != juan_keith_premise or juan_laurence_hypothesis != juan_laurence_premise:
    # check if the hypothesis contradicts the premise regarding the number of messages that Juan sends Keith and Laurence
    label = "contradiction"
elif laurence_missy_hypothesis != laurence_missy_premise:
    # check if the hypothesis contradicts the premise regarding the number of messages that Laurence sends Missy
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

