anita_work_days_premise = 18
indu_work_days_premise = 27
geeta_work_days_premise = 36

anita_work_days_hypothesis = 58
indu_work_days_hypothesis = 27
geeta_work_days_hypothesis = 36

# the hypothesis refers to the work days of Anita, Indu and Geeta mentioned in the premise
if anita_work_days_hypothesis!= anita_work_days_premise:
    # check if the number of work days for Anita in the hypothesis contradicts the number of work days in the premise
    label = "contradiction"
elif indu_work_days_hypothesis!= indu_work_days_premise:
    # check if the number of work days for Indu in the hypothesis contradicts the number of work days in the premise
    label = "contradiction"
elif geeta_work_days_hypothesis!= geeta_work_days_premise:
    # check if the number of work days for Geeta in the hypothesis contradicts the number of work days in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
