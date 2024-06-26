england_members_premise = 30
england_members_hypothesis = 30
france_members_premise = 26
france_members_hypothesis = 26
italy_members_premise = 32
italy_members_hypothesis = 32

# the hypothesis gives an estimate for the number of members traveling to England, France and Italy
# check if the hypothesis values contradict the premise ones
if england_members_hypothesis <= england_members_premise:
    label = "contradiction"
elif france_members_hypothesis!= france_members_premise:
    label = "contradiction"
elif italy_members_hypothesis!= italy_members_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
