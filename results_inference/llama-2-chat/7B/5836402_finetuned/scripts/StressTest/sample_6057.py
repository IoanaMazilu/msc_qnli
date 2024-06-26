anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36
anita_work_hypothesis = 38
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis refers to the work time of Anita, Indu and Geeta mentioned in the premise
if anita_work_hypothesis >= anita_work_premise:
    # check if the estimate of 'anita_work_hypothesis' contradicts the number of work days of Anita in the premise
    label = "contradiction"
elif indu_work_hypothesis!= indu_work_premise:
    # check if the number of work days of Indu in the hypothesis contradicts the number of work days of Indu reported in the premise
    label = "contradiction"
elif geeta_work_hypothesis!= geeta_work_premise:
    # check if the number of work days of Geeta in the hypothesis contradicts the number of work days of Geeta reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
