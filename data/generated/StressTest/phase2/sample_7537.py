# Premise: Reeya obtained less than 50, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Hypothesis: Reeya obtained 40, 60, 70, 80 and 80 out of 100 in different subjects, What will be the average.
# Golden Label: neutral

scores_premise = [50, 60, 70, 80, 80]
scores_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects, mentioned in the premise
if any(score_h >= score_p for score_h, score_p in zip(scores_hypothesis, scores_premise)):
    # check if any score in the hypothesis contradicts the premise (score_h should be less than score_p)
    label = "contradiction"
else:
    # if the hypothesis scores do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

