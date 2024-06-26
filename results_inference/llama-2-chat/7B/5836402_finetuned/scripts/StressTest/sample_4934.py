anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 58
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis refers to the work that Anita, Indu and Geeta can do, as mentioned in the premise
if anita_work_hypothesis!= anita_work_premise:
    # check if the work duration for Anita in the hypothesis contradicts the work duration in the premise
    label = "contradiction"
elif indu_work_hypothesis!= indu_work_premise:
    # check if the work duration for Indu in the hypothesis contradicts the work duration in the premise
    label = "contradiction"
elif geeta_work_hypothesis!= geeta_work_premise:
    # check if the work duration for Geeta in the hypothesis contradicts the work duration in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
