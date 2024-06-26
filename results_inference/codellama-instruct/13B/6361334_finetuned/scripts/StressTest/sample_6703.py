kiran_age_premise = 6
bineesh_age_premise = 9
kiran_age_hypothesis = 7
bineesh_age_hypothesis = 7

# the hypothesis refers to the age difference between Kiran and Bineesh, which is also mentioned in the premise
if kiran_age_hypothesis!= kiran_age_premise:
    # check if the hypothesis value contradicts the age difference in the premise
    label = "contradiction"
elif bineesh_age_hypothesis!= bineesh_age_premise:
    # check if the hypothesis value contradicts the ratio of ages in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
