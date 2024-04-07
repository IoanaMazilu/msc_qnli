# Premise: Sujeet joined him 2 months later, investing Rs.
# Hypothesis: Sujeet joined him 3 months later, investing Rs.
# Golden Label: contradiction

joining_time_premise = 2
joining_time_hypothesis = 3

# the hypothesis refers to the time Sujeet joined him, mentioned in the premise
if joining_time_premise != joining_time_hypothesis:
    # check if the time of joining in the hypothesis contradicts the time of joining in the premise
    label = "contradiction"
else:
    # the premise and the hypothesis are referring to the same event and the same time duration
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

