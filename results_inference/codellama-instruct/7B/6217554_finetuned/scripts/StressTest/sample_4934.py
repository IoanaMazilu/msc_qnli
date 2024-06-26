anita_indu_geeta_work_premise = 18
anita_indu_geeta_work_hypothesis = 58

# the hypothesis talks about the number of days Anita, Indu and Geeta can do a piece of work, referenced also in the premise
if anita_indu_geeta_work_hypothesis <= anita_indu_geeta_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'anita_indu_geeta_work_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Anita, Indu and Geeta can do a piece of work
    # any number of days greater than 'anita_indu_geeta_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
