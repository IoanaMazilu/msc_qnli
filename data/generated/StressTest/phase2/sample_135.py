# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him less than 6 months later, investing Rs.
# Golden Label: entailment

joining_time_premise = 2
joining_time_hypothesis = 6

# the hypothesis talks about the time when Jose joined, which is also mentioned in the premise
if joining_time_premise > joining_time_hypothesis:
    # check if the time when Jose joined in the premise contradicts the time mentioned in the hypothesis
    label = "contradiction"
elif joining_time_premise == joining_time_hypothesis:
    # check if the time when Jose joined in the premise is equivalent to the time mentioned in the hypothesis
    label = "contradiction"
else:
    # if the time when Jose joined in the premise does not contradict the time mentioned in the hypothesis
    # and since the premise does not give an exact value, we cannot infer entailment, so the relation is neutral
    label = "neutral"

print(label)

