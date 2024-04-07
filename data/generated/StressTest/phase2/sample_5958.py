# Premise: Last year 6 members of the club traveled to both England and France, no members traveled to both England and Italy, and 11 members traveled to both France and Italy.
# Hypothesis: Last year less than 8 members of the club traveled to both England and France, no members traveled to both England and Italy, and 11 members traveled to both France and Italy.
# Golden Label: entailment

eng_fra_travel_premise = 6
eng_fra_travel_hypothesis = 8
eng_ita_travel_premise = 0
eng_ita_travel_hypothesis = 0
fra_ita_travel_premise = 11
fra_ita_travel_hypothesis = 11

# the hypothesis refers to the number of club members who traveled to various countries mentioned in the premise
if eng_fra_travel_hypothesis < eng_fra_travel_premise:
    # check if the estimate of 'eng_fra_travel_hypothesis' contradicts the number of club members who traveled to England and France in the premise
    label = "contradiction"
elif eng_ita_travel_hypothesis != eng_ita_travel_premise:
    # check if the number of club members who traveled to England and Italy in the hypothesis contradicts the number of club members who traveled to England and Italy in the premise
    label = "contradiction"
elif fra_ita_travel_hypothesis != fra_ita_travel_premise:
    # check if the number of club members who traveled to France and Italy in the hypothesis contradicts the number of club members who traveled to France and Italy in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

