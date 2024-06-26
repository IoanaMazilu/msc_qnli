work_days_anita_premise = 18
work_days_indu_premise = 27
work_days_geeta_premise = 36
work_days_anita_hypothesis = 38
work_days_indu_hypothesis = 27
work_days_geeta_hypothesis = 36

# the hypothesis refers to the number of days taken by Anita, Indu and Geeta to complete a piece of work
if work_days_anita_hypothesis <= work_days_anita_premise or work_days_indu_hypothesis <= work_days_indu_premise or work_days_geeta_hypothesis <= work_days_geeta_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
