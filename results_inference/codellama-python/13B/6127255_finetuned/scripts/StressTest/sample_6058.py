anita_work_days_premise = 38
indu_work_days_premise = 27
geeta_work_days_premise = 36

anita_work_days_hypothesis = 18
indu_work_days_hypothesis = 27
geeta_work_days_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work, which is also mentioned in the premise
if anita_work_days_hypothesis >= anita_work_days_premise:
    # check if the number of days Anita can do the work in the hypothesis contradicts the estimate of less than 'anita_work_days_premise'
    label = "contradiction"
elif indu_work_days_hypothesis!= indu_work_days_premise or geeta_work_days_hypothesis!= geeta_work_days_premise:
    # check if the number of days Indu or Geeta can do the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Anita can do the work
    # any number of days less than 'anita_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
