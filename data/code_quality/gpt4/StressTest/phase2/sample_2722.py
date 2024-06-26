juan_to_laurence_premise = 1
juan_to_keith_premise = 2 * juan_to_laurence_premise
laurence_to_missy_premise = 7 * juan_to_laurence_premise

juan_to_laurence_hypothesis = 1
juan_to_keith_hypothesis = 2 * juan_to_laurence_hypothesis
laurence_to_missy_hypothesis = 8 * juan_to_laurence_hypothesis

# the hypothesis refers to the same situation and exact numbers of messages sent as described in the premise
if juan_to_keith_premise != juan_to_keith_hypothesis or juan_to_laurence_premise != juan_to_laurence_hypothesis:
    # check if the number of messages sent in the hypothesis contradicts the number of messages sent as reported in the premise
    label = "contradiction"
elif laurence_to_missy_hypothesis <= laurence_to_missy_premise:
    # check if the number of messages Laurence sends Missy in the hypothesis contradicts the estimate of more than 'laurence_to_missy_premise' 
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of messages Laurence sends Missy
    # any number of messages greater than 'laurence_to_missy_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
