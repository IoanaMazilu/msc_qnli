anita_work_days_premise = 18
indu_work_days_premise = 27
geeta_work_days_premise = 36

anita_work_days_hypothesis = 58
indu_work_days_hypothesis = 27
geeta_work_days_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work, mentioned in the premise
if anita_work_days_hypothesis!= anita_work_days_premise:
    # check if the number of days Anita can do the work in the hypothesis contradicts the number of days Anita can do the work in the premise
    label = "contradiction"
elif indu_work_days_hypothesis!= indu_work_days_premise:
    # check if the number of days Indu can do the work in the hypothesis contradicts the number of days Indu can do the work in the premise
    label = "contradiction"
elif geeta_work_days_hypothesis!= geeta_work_days_premise:
    # check if the number of days Geeta can do the work in the hypothesis contradicts the number of days Geeta can do the work in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
