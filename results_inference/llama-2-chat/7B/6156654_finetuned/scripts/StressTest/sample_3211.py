work_days_premise = 40
work_days_hypothesis = 20
finish_days_premise = 30
finish_days_hypothesis = 30

# the hypothesis talks about the number of days worked and finished by Rajesh
if work_days_hypothesis >= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the premise
    label = "contradiction"
elif finish_days_hypothesis!= finish_days_premise:
    # check if the number of finish days in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
