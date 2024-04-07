# Premise: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year less than 46 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: entailment

members_england_premise = 26
members_england_hypothesis = 46
members_france_premise = 26
members_france_hypothesis = 26
members_italy_premise = 32
members_italy_hypothesis = 32

# the hypothesis talks about the number of club members that traveled to England, France, and Italy
if members_england_premise >= members_england_hypothesis:
    # check if the number of members that traveled to England in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif members_france_premise != members_france_hypothesis or members_italy_premise != members_italy_hypothesis:
    # check if the number of members that traveled to France or Italy in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

