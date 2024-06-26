england_members_premise = 30
england_members_hypothesis = 30
france_members_premise = 26
france_members_hypothesis = 26
italy_members_premise = 32
italy_members_hypothesis = 32

# the hypothesis refers to the number of club members who traveled to England, France and Italy
if england_members_hypothesis <= england_members_premise:
    # check if the hypothesis value contradicts the exact number of england members in the premise
    label = "contradiction"
elif french_members_hypothesis!= french_members_premise:
    # check if the number of France members in the hypothesis contradicts the number of France members in the premise
    label = "contradiction"
elif italy_members_hypothesis!= italy_members_premise:
    # check if the number of Italy members in the hypothesis contradicts the number of Italy members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
