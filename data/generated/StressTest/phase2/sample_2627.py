# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him 6 months later, investing Rs.
# Golden Label: contradiction

join_time_premise = 2
join_time_hypothesis = 6

# the hypothesis refers to the time when Jose joined him, mentioned also in the premise
if join_time_hypothesis != join_time_premise:
    # check if the join time in the hypothesis contradicts the join time reported in the premise
    label = "contradiction"
else:
    # if the join time in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

