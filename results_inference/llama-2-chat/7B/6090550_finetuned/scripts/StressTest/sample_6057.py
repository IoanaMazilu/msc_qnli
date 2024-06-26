work_days_anita = 18
work_days_indu = 27
work_days_geeta = 36
work_days_hypothesis = 38

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work
if work_days_anita >= work_days_hypothesis:
    # check if the number of days Anita can do the work contradicts the hypothesis
    label = "contradiction"
elif work_days_indu >= work_days_hypothesis or work_days_geeta >= work_days_hypothesis:
    # check if the number of days Indu or Geeta can do the work contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of days Anita, Indu and Geeta can do the work is less than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
