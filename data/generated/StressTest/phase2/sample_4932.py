# Premise: Anita, Indu and Geeta can do a piece of work in 18 days, 27 days and 36 days respectively.
# Hypothesis: Anita, Indu and Geeta can do a piece of work in less than 68 days, 27 days and 36 days respectively.
# Golden Label: entailment

anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 68
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis refers to the time Anita, Indu and Geeta take to complete a work, the same as in the premise
if anita_work_hypothesis <= anita_work_premise and indu_work_hypothesis == indu_work_premise and geeta_work_hypothesis == geeta_work_premise:
    # check if the time estimates in the hypothesis contradict the times reported in the premise
    label = "contradiction"
elif anita_work_hypothesis > anita_work_premise or indu_work_hypothesis != indu_work_premise or geeta_work_hypothesis != geeta_work_premise:
    # check if the time estimates in the hypothesis are exactly the same as in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and are exactly the same, we can infer entailment
    label = "entailment"

print(label)

