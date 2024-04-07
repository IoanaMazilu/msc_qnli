# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him more than 2 months later, investing Rs.
# Golden Label: contradiction

join_time_premise = 2
join_time_hypothesis = 2

# the hypothesis talks about the time Jose joined him, which is also referenced in the premise
if join_time_hypothesis > join_time_premise:
    # check if the hypothesis time contradicts the precise time 'join_time_premise' in the premise
    label = "contradiction"
elif join_time_hypothesis < join_time_premise:
    # check if the hypothesis time is less than the time 'join_time_premise' in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

