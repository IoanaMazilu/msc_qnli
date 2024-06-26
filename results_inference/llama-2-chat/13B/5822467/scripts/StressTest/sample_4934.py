anita_days_premise = 18
indu_days_premise = 27
geeta_days_premise = 36

anita_days_hypothesis = 58
indu_days_hypothesis = 27
geeta_days_hypothesis = 36

# the hypothesis refers to the number of days taken by each person to complete the work
if anita_days_hypothesis <= anita_days_premise:
    # check if the estimate of 'anita_days_hypothesis' contradicts the number of days reported in the premise
    label = "contradiction"
elif indu_days_hypothesis!= indu_days_premise:
    # check if the number of days taken by Indu in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif geeta_days_hypothesis!= geeta_days_premise:
    # check if the number of days taken by Geeta in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
