father_age_premise = 38
mother_age_premise = 36
brother_age_premise = 4

father_age_hypothesis = 18
mother_age_hypothesis = 36
brother_age_hypothesis = 4

# the hypothesis refers to the age of Ayesha's father and mother, mentioned in the premise
if father_age_hypothesis <= father_age_premise and mother_age_hypothesis <= mother_age_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif brother_age_hypothesis!= brother_age_premise:
    # check if the age of Ayesha's brother in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
