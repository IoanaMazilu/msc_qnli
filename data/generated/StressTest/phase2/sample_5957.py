# Premise: Last year 26 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Hypothesis: Last year 86 members of a certain club traveled to England, 26 members traveled to France, and 32 members traveled to Italy.
# Golden Label: contradiction

england_travelers_premise = 26
england_travelers_hypothesis = 86
france_travelers_premise = 26
france_travelers_hypothesis = 26
italy_travelers_premise = 32
italy_travelers_hypothesis = 32

# The hypothesis talks about the number of club members that travelled to England, France, and Italy, same as the premise
if england_travelers_hypothesis != england_travelers_premise:
    # Check if the number of travelers to England in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif france_travelers_hypothesis != france_travelers_premise:
    # Check if the number of travelers to France in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif italy_travelers_hypothesis != italy_travelers_premise:
    # Check if the number of travelers to Italy in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

