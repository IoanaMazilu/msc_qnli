# Premise: Calculate Rebecca's average score in an exam if she obtained the following marks more than 10, 57, 69, 89 and 85 out of 100 in different subjects.
# Hypothesis: Calculate Rebecca's average score in an exam if she obtained the following marks 70, 57, 69, 89 and 85 out of 100 in different subjects.
# Golden Label: neutral

# define the numerical entities in the premise
exam_scores_premise = [10, 57, 69, 89, 85]

# define the numerical entities in the hypothesis
exam_scores_hypothesis = [70, 57, 69, 89, 85]

# calculate the average score in the premise and the hypothesis
average_score_premise = sum(exam_scores_premise) / len(exam_scores_premise)
average_score_hypothesis = sum(exam_scores_hypothesis) / len(exam_scores_hypothesis)

# the hypothesis refers to the average exam score of Rebecca which is also mentioned in the premise
if average_score_premise != average_score_hypothesis:
    # check if the average exam score in the hypothesis contradicts the average exam score in the premise
    label = "contradiction"
else:
    # if the average exam score in the hypothesis does not contradict the average exam score in the premise, we can infer entailment
    label = "entailment"

print(label)

