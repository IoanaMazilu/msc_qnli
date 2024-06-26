anita_indu_geeta_work_premise = 18
anita_indu_geeta_work_hypothesis = 38

# the hypothesis refers to the number of days Anita, Indu and Geeta can do a piece of work, mentioned in the premise
if anita_indu_geeta_work_hypothesis <= anita_indu_geeta_work_premise:
    # check if the estimate of 'anita_indu_geeta_work_hypothesis' contradicts the number of days Anita, Indu and Geeta can do a piece of work in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
