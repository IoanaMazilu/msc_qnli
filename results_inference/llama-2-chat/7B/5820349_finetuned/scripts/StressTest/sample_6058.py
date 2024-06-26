anita_work_time_premise = 38
indu_work_time_premise = 27
geeta_work_time_premise = 36

anita_work_time_hypothesis = 18
indu_work_time_hypothesis = 27
geeta_work_time_hypothesis = 36

# the hypothesis refers to the time Anita, Indu and Geeta need to complete a piece of work, as mentioned in the premise
if anita_work_time_hypothesis >= anita_work_time_premise:
    # check if the estimate of 'anita_work_time_hypothesis' contradicts the time Anita needs in the premise
    label = "contradiction"
elif indu_work_time_hypothesis!= indu_work_time_premise or geeta_work_time_hypothesis!= geeta_work_time_premise:
    # check if the time Indu or Geeta needs in the hypothesis contradicts the time they need in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
