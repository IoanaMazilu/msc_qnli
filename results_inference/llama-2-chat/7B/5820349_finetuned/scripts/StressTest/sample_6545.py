father_age_premise = 38
father_age_hypothesis = 18
mother_age_premise = 36
mother_age_hypothesis = 36

# the hypothesis refers to the age of Ayesha's parents at the time of her and her brother's birth
if father_age_premise!= father_age_hypothesis:
    # check if the age of Ayesha's father at the time of her birth contradicts the age mentioned in the hypothesis
    label = "contradiction"
elif mother_age_premise!= mother_age_hypothesis:
    # check if the age of Ayesha's mother at the time of her brother's birth contradicts the age mentioned in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
