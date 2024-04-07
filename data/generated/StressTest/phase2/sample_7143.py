# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was 38.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was less than 48.
# Golden Label: entailment

average_score_premise = 38
average_score_hypothesis = 48

# the hypothesis refers to the same average golf score mentioned in the premise
if average_score_premise >= average_score_hypothesis:
    # check if the 'average_score_premise' contradicts the hypothesis that the average score was less than 'average_score_hypothesis'
    label = "contradiction"
else:
    # if the premise value doesn't contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

