# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was 28.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was 18.
# Golden Label: contradiction

average_score_premise = 28
average_score_hypothesis = 18

# the hypothesis refers to the average golf score mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average score in the hypothesis contradicts the average score reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

