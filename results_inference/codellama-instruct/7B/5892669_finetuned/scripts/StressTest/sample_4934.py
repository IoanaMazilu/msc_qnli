work_days_Anita_premise = 18
work_days_Indu_premise = 27
work_days_Geeta_premise = 36

work_days_Anita_hypothesis = 58
work_days_Indu_hypothesis = 27
work_days_Geeta_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work, mentioned in the premise
if work_days_Anita_hypothesis!= work_days_Anita_premise:
    # check if the number of days Anita can do the work in the hypothesis contradicts the number of days Anita can do the work in the premise
    label = "contradiction"
elif work_days_Indu_hypothesis!= work_days_Indu_premise:
    # check if the number of days Indu can do the work in the hypothesis contradicts the number of days Indu can do the work in the premise
    label = "contradiction"
elif work_days_Geeta_hypothesis!= work_days_Geeta_premise:
    # check if the number of days Geeta can do the work in the hypothesis contradicts the number of days Geeta can do the work in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
