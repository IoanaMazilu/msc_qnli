# Premise: Calculate Ronald's average score in an exam if he obtained the following marks 51, 57, 68, 60 and 78 out of 100 in different subjects.
# Hypothesis: Calculate Ronald's average score in an exam if he obtained the following marks more than 21, 57, 68, 60 and 78 out of 100 in different subjects.
# Golden Label: entailment

# Scores obtained by Ronald in different subjects as per premise and hypothesis
scores_premise = [51, 57, 68, 60, 78]
scores_hypothesis = [21, 57, 68, 60, 78]

# Calculating average scores for premise and hypothesis
average_score_premise = sum(scores_premise) / len(scores_premise)
average_score_hypothesis = sum(scores_hypothesis) / len(scores_hypothesis)

# If the average score as per hypothesis is less than or equal to average score as per premise, it's a contradiction
if average_score_hypothesis <= average_score_premise:
    label = "contradiction"
else:
    # If average score as per hypothesis is more than average score as per premise, it's neutral as it can't be explicitly entailed from the premise
    label = "neutral"

print(label)

