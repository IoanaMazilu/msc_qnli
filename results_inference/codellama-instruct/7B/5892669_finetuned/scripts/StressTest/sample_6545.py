father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the age of Ayesha's parents at the time of her and her brother's birth, mentioned in the premise
if father_age_premise!= father_age_hypothesis:
    # check if the age of Ayesha's father in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the age of Ayesha's mother in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
