# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him less than 7 months later, investing Rs.
# Golden Label: entailment

joining_time_premise = 2
joining_time_hypothesis = 7

# the hypothesis provides a time frame of Jose joining, which is also mentioned in the premise
if joining_time_premise > joining_time_hypothesis:
    # check if the joining time in the premise contradicts the estimate of less than 'joining_time_hypothesis' months
    label = "contradiction"
elif joining_time_premise < joining_time_hypothesis:
    # if the joining time mentioned in the premise does not contradict the one in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the joining time in the premise and hypothesis are the same, it is a neutral case
    label = "neutral"

print(label)

