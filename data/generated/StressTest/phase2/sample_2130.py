# Premise: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 30 members traveled to Italy.
# Hypothesis: Last year less than 46 members of a certain club traveled to England, 26 members traveled to France, and 30 members traveled to Italy.
# Golden Label: entailment

travel_england_premise = 26
travel_england_hypothesis = 46
travel_france_premise = 26
travel_france_hypothesis = 26
travel_italy_premise = 30
travel_italy_hypothesis = 30

# the hypothesis refers to the number of members who traveled to England, France and Italy, mentioned in the premise
if travel_england_hypothesis <= travel_england_premise:
    # check if the estimate of 'travel_england_hypothesis' contradicts the number of members who traveled to England in the premise
    label = "contradiction"
elif travel_france_hypothesis != travel_france_premise or travel_italy_hypothesis != travel_italy_premise:
    # check if the number of members who traveled to France and Italy in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

