# Premise: Reeya obtained more than 20, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 50, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Golden Label: neutral

# Define variables
scores_premise = [20, 60, 70, 80, 80]  # scores obtained by Reeya in premise
scores_hypothesis = [50, 60, 70, 80, 80]  # scores obtained by Reeya in hypothesis

# Compare each score in hypothesis with the corresponding score in premise
for score_p, score_h in zip(scores_premise, scores_hypothesis):
    if score_h <= score_p:
        # check if the score in hypothesis contradicts the statement "more than score_p" in premise
        label = "contradiction"
        break
else:
    # the premise gives only an estimate for the scores
    # any score greater than the corresponding score in premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

