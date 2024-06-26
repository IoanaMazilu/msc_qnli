work_days_anita_premise = 38
work_days_anita_hypothesis = 18
work_days_indu_premise = 27
work_days_indu_hypothesis = 27
work_days_geeta_premise = 36
work_days_geeta_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta need to do a piece of work, mentioned in the premise
if work_days_anita_hypothesis >= work_days_anita_premise:
    # check if the estimate of 'work_days_anita_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif work_days_indu_hypothesis!= work_days_indu_premise:
    # check if the number of days in Indu's case in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif work_days_geeta_hypothesis!= work_days_geeta_premise:
    # check if the number of days in Geeta's case in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days for Anita and Geeta
    # any number of days less than 'work_days_anita_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
