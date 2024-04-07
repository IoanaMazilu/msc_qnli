# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him less than 3 months later, investing Rs.
# Golden Label: entailment

join_time_premise = 2
join_time_hypothesis = 3

# the hypothesis refers to the time Jose joined, which is also mentioned in the premise
if join_time_hypothesis < join_time_premise:
    # check if the estimate of 'join_time_hypothesis' contradicts the time in the premise
    label = "contradiction"
elif join_time_hypothesis > join_time_premise:
    # check if the time in the hypothesis is more than the time reported in the premise
    label = "entailment"
else:
    # if the hypothesis time and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

