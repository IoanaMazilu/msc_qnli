members_premise = 26
members_hypothesis = 86

# the hypothesis refers to the number of members of a certain club who traveled to different countries
if members_hypothesis >= (members_premise + members_premise):
    # check if the estimate of'members_hypothesis' contradicts the sum of the number of members who traveled to England, France, and Italy in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of members who traveled to each country, and the hypothesis value is consistent with those estimates
    label = "entailment"

print(label)
