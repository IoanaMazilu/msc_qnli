father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36
brother_age_premise = 4
brother_age_hypothesis = 4

# the hypothesis refers to the age of Ayesha's father and mother, which are also mentioned in the premise
if father_age_hypothesis!= father_age_premise:
    # check if the age of Ayesha's father in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the age of Ayesha's mother in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif brother_age_hypothesis!= brother_age_premise:
    # check if the age of Ayesha's brother in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
