# Premise: Anita, Indu and Geeta can do a piece of work in 18 days, 27 days and 36 days respectively.
# Hypothesis: Anita, Indu and Geeta can do a piece of work in less than 38 days, 27 days and 36 days respectively.
# Golden Label: entailment

anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 38
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis refers to the time Anita, Indu and Geeta need to complete a job, mentioned in the premise
if anita_work_hypothesis < anita_work_premise:
    # check if the hypothesis value contradicts the time Anita takes to do the job in the premise
    label = "contradiction"
elif indu_work_hypothesis != indu_work_premise:
    # check if the time Indu takes to do the job in the hypothesis contradicts the time Indu takes to do the job in the premise
    label = "contradiction"
elif geeta_work_hypothesis != geeta_work_premise:
    # check if the time Geeta takes to do the job in the hypothesis contradicts the time Geeta takes to do the job in the premise
    label = "contradiction"
else:
    # the hypothesis estimates for the time to complete the work do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

