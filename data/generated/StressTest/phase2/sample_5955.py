# Premise: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year less than 56 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: entailment

members_england_premise = 26
members_england_hypothesis = 56
members_france_premise = 26
members_france_hypothesis = 26
members_italy_premise = 32
members_italy_hypothesis = 32

# the hypothesis discusses the number of members who traveled to England, France, and Italy
# these numbers are also referenced in the premise
if members_england_hypothesis <= members_england_premise:
    # check if the hypothesis estimate of less than 'members_england_hypothesis' contradicts the number of members who traveled to England in the premise
    label = "contradiction"
elif members_france_hypothesis != members_france_premise:
    # check if the number of members who traveled to France in the hypothesis contradicts the number of members who traveled to France in the premise
    label = "contradiction"
elif members_italy_hypothesis != members_italy_premise:
    # check if the number of members who traveled to Italy in the hypothesis contradicts the number of members who traveled to Italy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

