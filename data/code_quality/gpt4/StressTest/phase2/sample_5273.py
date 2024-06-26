juan_to_keith_premise = 3
juan_to_laurence_premise = 1
laurence_to_missy_premise = 2 * juan_to_laurence_premise

juan_to_keith_hypothesis = 3
juan_to_laurence_hypothesis = 1
laurence_to_missy_hypothesis = 2 * juan_to_laurence_hypothesis - 1

# the hypothesis refers to the number of messages sent and received by Juan, Keith, Laurence, and Missy mentioned in the premise
if juan_to_keith_premise != juan_to_keith_hypothesis or juan_to_laurence_premise != juan_to_laurence_hypothesis:
    # check if the number of messages sent by Juan to Keith or Laurence in the hypothesis contradicts the number of messages sent in the premise
    label = "contradiction"
elif laurence_to_missy_hypothesis >= laurence_to_missy_premise:
    # check if the number of messages sent by Laurence to Missy in the hypothesis contradicts the number of messages sent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
