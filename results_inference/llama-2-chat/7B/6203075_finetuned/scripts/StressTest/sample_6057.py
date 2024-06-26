anita_work_days_premise = 18
indu_work_days_premise = 27
geeta_work_days_premise = 36

anita_work_days_hypothesis = 38
indu_work_days_hypothesis = 27
geeta_work_days_hypothesis = 36

# the hypothesis refers to the work days of Anita, Indu and Geeta
if anita_work_days_premise >= anita_work_days_hypothesis:
    # check if the estimate of 'anita_work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif indu_work_days_premise!= indu_work_days_hypothesis or geeta_work_days_premise!= geeta_work_days_hypothesis:
    # check if the number of work days for Indu or Geeta in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
