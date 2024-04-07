# Premise: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 30 members traveled to Italy.
# Hypothesis: Last year 86 members of a certain club traveled to England, 26 members traveled to France, and 30 members traveled to Italy.
# Golden Label: contradiction

members_england_premise = 26
members_france_premise = 26
members_italy_premise = 30

members_england_hypothesis = 86
members_france_hypothesis = 26
members_italy_hypothesis = 30

# the hypothesis refers to the number of members who traveled to England, France and Italy, as mentioned in the premise
if members_england_hypothesis != members_england_premise:
    # check if the number of members who traveled to England in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif members_france_hypothesis != members_france_premise:
    # check if the number of members who traveled to France in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif members_italy_hypothesis != members_italy_premise:
    # check if the number of members who traveled to Italy in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

