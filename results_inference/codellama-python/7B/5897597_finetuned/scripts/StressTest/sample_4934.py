work_days_anita_premise = 18
work_days_anita_hypothesis = 58
work_days_indu_premise = 27
work_days_indu_hypothesis = 27
work_days_geeta_premise = 36
work_days_geeta_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta need to complete a piece of work, mentioned in the premise
if work_days_anita_premise!= work_days_anita_hypothesis:
    # check if the number of days Anita needs in the hypothesis contradicts the number of days Anita needs in the premise
    label = "contradiction"
elif work_days_indu_premise!= work_days_indu_hypothesis:
    # check if the number of days Indu needs in the hypothesis contradicts the number of days Indu needs in the premise
    label = "contradiction"
elif work_days_geeta_premise!= work_days_geeta_hypothesis:
    # check if the number of days Geeta needs in the hypothesis contradicts the number of days Geeta needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)