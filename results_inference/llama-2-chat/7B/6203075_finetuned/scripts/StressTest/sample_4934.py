anita_work_days_premise = 18
indu_work_days_premise = 27
geeta_work_days_premise = 36

anita_work_days_hypothesis = 58
indu_work_days_hypothesis = 27
geeta_work_days_hypothesis = 36

# the hypothesis talks about the number of days Anita, Indu and Geeta can do a piece of work, which are also mentioned in the premise
if anita_work_days_hypothesis!= anita_work_days_premise or \
   indu_work_days_hypothesis!= indu_work_days_premise or \
   geeta_work_days_hypothesis!= geeta_work_days_premise:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
