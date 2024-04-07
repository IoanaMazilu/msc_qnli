# Premise: Scott's average (arithmetic mean) golf score on his first four rounds was 18.
# Hypothesis: Scott's average (arithmetic mean) golf score on his first four rounds was less than 48.
# Golden Label: entailment

average_score_premise = 18
average_score_hypothesis = 48

# the hypothesis refers to the average golf score on first four rounds mentioned in the premise
if average_score_premise > average_score_hypothesis:
    # check if the average golf score in the premise contradicts the estimate of 'average_score_hypothesis'
    label = "contradiction"
elif average_score_premise < average_score_hypothesis:
    # if average golf score in the premise is less than the 'average_score_hypothesis', we can infer entailment
    label = "entailment"
else:
    label = "neutral"

print(label)

