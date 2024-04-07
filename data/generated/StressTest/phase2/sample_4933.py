# Premise: Anita, Indu and Geeta can do a piece of work in less than 68 days, 27 days and 36 days respectively.
# Hypothesis: Anita, Indu and Geeta can do a piece of work in 18 days, 27 days and 36 days respectively.
# Golden Label: neutral

anita_work_premise = 68
indu_work_premise = 27
geeta_work_premise = 36

anita_work_hypothesis = 18
indu_work_hypothesis = 27
geeta_work_hypothesis = 36

# the hypothesis talks about the time Anita, Indu and Geeta can take to do a piece of work, referenced also in the premise
if anita_work_hypothesis >= anita_work_premise or indu_work_hypothesis >= indu_work_premise or geeta_work_hypothesis >= geeta_work_premise:
    # check if the hypothesis values contradict the estimates of less than 'anita_work_premise', 'indu_work_premise' and 'geeta_work_premise' 
    label = "contradiction"
else:
    # the premise gives only an estimate for the time each person can take to do a piece of work
    # any time less than 'anita_work_premise', 'indu_work_premise' and 'geeta_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

