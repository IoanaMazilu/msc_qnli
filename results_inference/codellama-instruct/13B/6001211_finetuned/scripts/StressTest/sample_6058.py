work_days_premise = 38
work_days_indu_premise = 27
work_days_geeta_premise = 36

work_days_hypothesis = 18
work_days_indu_hypothesis = 27
work_days_geeta_hypothesis = 36

# the hypothesis refers to the number of days Anita, Indu and Geeta can complete a piece of work, as mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the number of days in the hypothesis contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
elif work_days_indu_hypothesis!= work_days_indu_premise or work_days_geeta_hypothesis!= work_days_geeta_premise:
    # check if the number of days for Indu or Geeta in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
