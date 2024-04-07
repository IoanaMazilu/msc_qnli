# Premise: Last year less than 46 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: neutral

england_travelers_premise = 46
england_travelers_hypothesis = 26
france_travelers_premise = 26
france_travelers_hypothesis = 26
italy_travelers_premise = 32
italy_travelers_hypothesis = 32

# the hypothesis talks about the number of club members who traveled to England, France, and Italy, referenced also in the premise
if england_travelers_hypothesis >= england_travelers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'england_travelers_premise' 
    label = "contradiction"
elif france_travelers_hypothesis != france_travelers_premise or italy_travelers_hypothesis != italy_travelers_premise:
    # check if the number of club members who traveled to France or Italy in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

