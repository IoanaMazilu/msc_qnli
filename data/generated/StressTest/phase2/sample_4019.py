# Premise: Calculate Ronald's average score in an exam if he obtained the following marks 51, 57, 68, 60 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Ronald's average score in an exam if he obtained the following marks 21, 57, 68, 60 and 78 out of 100 in different subjects.
# Golden Label: contradiction

# scores obtained by Ronald in the premise and hypothesis
ronald_scores_premise = [51, 57, 68, 60, 78]
ronald_scores_hypothesis = [21, 57, 68, 60, 78]

# calculate average score in the premise and hypothesis
average_score_premise = sum(ronald_scores_premise) / len(ronald_scores_premise)
average_score_hypothesis = sum(ronald_scores_hypothesis) / len(ronald_scores_hypothesis)

# compare average scores in the premise and hypothesis
if average_score_premise == average_score_hypothesis:
    # if average scores are exactly the same, then it's entailment
    label = "entailment"
elif average_score_premise != average_score_hypothesis:
    # if average scores are different, then it's contradiction
    label = "contradiction"

print(label)

