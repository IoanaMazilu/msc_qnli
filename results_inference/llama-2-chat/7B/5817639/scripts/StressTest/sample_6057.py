anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 38
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis talks about the time it takes for Anita, Indu and Geeta to do a piece of work, referenced also in the premise
if anita_work_hypothesis <= anita_work_premise:
    # check if the hypothesis value contradicts the estimate of less than 'anita_work_premise'
    label = "contradiction"
elif indu_work_hypothesis!= indu_work_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
