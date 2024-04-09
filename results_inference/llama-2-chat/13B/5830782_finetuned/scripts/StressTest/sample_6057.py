work_days_anita_premise = 18
work_days_indu_premise = 27
work_days_geeta_premise = 36

work_days_anita_hypothesis = 38
work_days_indu_hypothesis = 27
work_days_geeta_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work, which is also mentioned in the premise
if work_days_anita_hypothesis <= work_days_anita_premise:
    # check if the estimate of 'work_days_anita_hypothesis' contradicts the number of days Anita can do the work in the premise
    label = "contradiction"
elif work_days_indu_hypothesis!= work_days_indu_premise:
    # check if the number of days Indu can do the work in the hypothesis contradicts the number of days Indu can do the work in the premise
    label = "contradiction"
elif work_days_geeta_hypothesis!= work_days_geeta_premise:
    # check if the number of days Geeta can do the work in the hypothesis contradicts the number of days Geeta can do the work in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
