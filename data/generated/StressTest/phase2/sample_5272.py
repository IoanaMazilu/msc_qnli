# Premise: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy more than 1 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 2 times as many messages as he receives from Juan.
# Golden Label: neutral

juan_to_laurence_premise = 1
juan_to_keith_premise = 3 * juan_to_laurence_premise
laurence_to_missy_premise = 1 * juan_to_laurence_premise

juan_to_laurence_hypothesis = 1
juan_to_keith_hypothesis = 3 * juan_to_laurence_hypothesis
laurence_to_missy_hypothesis = 2 * juan_to_laurence_hypothesis

# the hypothesis refers to the number of messages exchanged between Juan, Keith, Laurence and Missy in a day, mentioned in the premise
if juan_to_laurence_hypothesis != juan_to_laurence_premise or juan_to_keith_hypothesis != juan_to_keith_premise:
    # check if the number of messages sent from Juan to Laurence or Keith in the hypothesis contradicts the number of messages reported in the premise
    label = "contradiction"
elif laurence_to_missy_hypothesis <= laurence_to_missy_premise:
    # check if the number of messages sent from Laurence to Missy in the hypothesis contradicts the number of messages sent in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of messages sent from Laurence to Missy
    # any number of messages greater than 'laurence_to_missy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

