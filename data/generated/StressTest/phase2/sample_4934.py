# Premise: Anita, Indu and Geeta can do a piece of work in 18 days, 27 days and 36 days respectively.
# Hypothesis: Anita, Indu and Geeta can do a piece of work in 58 days, 27 days and 36 days respectively.
# Golden Label: contradiction

anita_work_premise = 18
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 58
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis refers to the time Anita, Indu, and Geeta take to do a piece of work, mentioned in the premise
if anita_work_premise != anita_work_hypothesis:
    # check if the time Anita takes to do the work in the hypothesis contradicts the time in the premise
    label = "contradiction"
elif indu_work_premise != indu_work_hypothesis:
    # check if the time Indu takes to do the work in the hypothesis contradicts the time in the premise
    label = "contradiction"
elif geeta_work_premise != geeta_work_hypothesis:
    # check if the time Geeta takes to do the work in the hypothesis contradicts the time in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

