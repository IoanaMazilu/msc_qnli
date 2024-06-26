father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36
brother_age_premise = 4
brother_age_hypothesis = 4

# the hypothesis talks about the ages of Ayesha's parents and brother at different points in time, referenced also in the premise
if father_age_hypothesis!= father_age_premise:
    # check if the estimate of 'father_age_hypothesis' contradicts the age of Ayesha's father reported in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the number of Ayesha's mother's age in the hypothesis contradicts the number of her mother's age reported in the premise
    label = "contradiction"
elif brother_age_hypothesis!= brother_age_premise:
    # check if the number of Ayesha's brother's age in the hypothesis contradicts the number of her brother's age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
