# Premise: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy less than 6 times as many messages as he receives from Juan.
# Hypothesis: In one day, Juan sends Keith three times as many messages as he sends Laurence, and Laurence sends Missy 5 times as many messages as he receives from Juan.
# Golden Label: neutral

juan_to_laurence_premise = 1
juan_to_keith_premise = 3 * juan_to_laurence_premise
laurence_to_missy_upper_bound_premise = 6 * juan_to_laurence_premise

juan_to_laurence_hypothesis = 1
juan_to_keith_hypothesis = 3 * juan_to_laurence_hypothesis
laurence_to_missy_hypothesis = 5 * juan_to_laurence_hypothesis

# the hypothesis talks about the number of messages sent by Juan to Keith and Laurence, and by Laurence to Missy, referenced also in the premise
if juan_to_keith_hypothesis != juan_to_keith_premise or juan_to_laurence_hypothesis != juan_to_laurence_premise:
    # check if the number of messages sent by Juan in the hypothesis contradicts the number of messages sent by Juan reported in the premise
    label = "contradiction"
elif laurence_to_missy_hypothesis > laurence_to_missy_upper_bound_premise:
    # check if the number of messages sent by Laurence in the hypothesis contradicts the estimate of less than 'laurence_to_missy_upper_bound_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

