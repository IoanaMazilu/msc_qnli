anti_war_members_premise = 3
anti_war_members_hypothesis = 2

# the hypothesis mentions the number of anti-war members considering supporting expanded military action, which is also referenced in the premise
if anti_war_members_hypothesis!= anti_war_members_premise:
    # check if the number of anti-war members in the hypothesis contradicts the number of anti-war members in the premise
    label = "contradiction"
else:
    # if the number of anti-war members in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
