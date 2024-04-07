# Premise: Last year 30 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year less than 70 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: entailment

england_travelers_premise = 30
france_travelers_premise = 26
italy_travelers_premise = 32

england_travelers_hypothesis = 70
france_travelers_hypothesis = 26
italy_travelers_hypothesis = 32

# the hypothesis refers to the number of club members who traveled to England, France and Italy, mentioned in the premise
if england_travelers_hypothesis < england_travelers_premise:
    # check if the estimate of 'england_travelers_hypothesis' contradicts the number of members who traveled to England in the premise
    label = "contradiction"
elif france_travelers_hypothesis != france_travelers_premise or italy_travelers_hypothesis != italy_travelers_premise:
    # check if the number of members who traveled to France or Italy in the hypothesis contradicts the number of members who traveled to these countries reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

