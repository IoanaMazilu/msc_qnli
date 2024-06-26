anita_work_days = 18
indu_work_days = 27
geeta_work_days = 36
total_work_days = 38

# the hypothesis refers to the number of days required by Anita, Indu, and Geeta to complete a piece of work
# according to the premise, Anita, Indu, and Geeta can do a piece of work in 18, 27, and 36 days respectively
if anita_work_days >= total_work_days:
    # check if Anita's work days contradict the hypothesis
    label = "contradiction"
elif indu_work_days >= total_work_days:
    # check if Indu's work days contradict the hypothesis
    label = "contradiction"
elif geeta_work_days >= total_work_days:
    # check if Geeta's work days contradict the hypothesis
    label = "contradiction"
else:
    # if the premise values do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
