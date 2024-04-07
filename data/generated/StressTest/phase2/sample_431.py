# Premise: Last year 12 members of the club traveled to both England and France, 6 members traveled to both England and Italy, and 0 members traveled to both France and Italy.
# Hypothesis: Last year less than 12 members of the club traveled to both England and France, 6 members traveled to both England and Italy, and 0 members traveled to both France and Italy.
# Golden Label: contradiction

members_england_france_premise = 12
members_england_france_hypothesis = 12
members_england_italy_premise = 6
members_england_italy_hypothesis = 6
members_france_italy_premise = 0
members_france_italy_hypothesis = 0

# the hypothesis provides exact numbers which should match the ones from the premise
if members_england_france_hypothesis >= members_england_france_premise:
    # check if the hypothesis value contradicts the premise 'members_england_france_premise'
    label = "contradiction"
elif members_england_italy_hypothesis != members_england_italy_premise or members_france_italy_hypothesis != members_france_italy_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

