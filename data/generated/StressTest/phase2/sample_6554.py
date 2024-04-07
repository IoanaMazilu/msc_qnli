# Premise: Last year 30 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year more than 30 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: contradiction

england_travelers_premise = 30
france_travelers_premise = 26
italy_travelers_premise = 32

england_travelers_hypothesis = 30
france_travelers_hypothesis = 26
italy_travelers_hypothesis = 32

# hypothesis suggests that more than 'england_travelers_hypothesis' members traveled to England
if england_travelers_premise != england_travelers_hypothesis:
    # check if the number of members who traveled to England as per hypothesis contradicts the number given in premise
    label = "contradiction"
elif france_travelers_hypothesis != france_travelers_premise:
    # check if the number of members who traveled to France as per hypothesis contradicts the number given in premise
    label = "contradiction"
elif italy_travelers_hypothesis != italy_travelers_premise:
    # check if the number of members who traveled to Italy as per hypothesis contradicts the number given in premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

