father_age_premise = 38
mother_age_premise = 36
brother_age_premise = 4
father_age_hypothesis = 18
mother_age_hypothesis = 36

# the hypothesis refers to the ages of Ayesha's father and mother at the time of her birth and the birth of her brother
if father_age_hypothesis!= father_age_premise:
    # check if the age of Ayesha's father in the hypothesis contradicts his age in the premise
    label = "contradiction"
elif mother_age_hypothesis!= mother_age_premise:
    # check if the age of Ayesha's mother in the hypothesis contradicts her age in the premise
    label = "contradiction"
else:
    # if the ages of Ayesha's father and mother in the hypothesis do not contradict their ages in the premise, we can infer entailment
    label = "entailment"

print(label)
