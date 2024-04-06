# Premise: Three of the key anti-war members of Congress are considering supporting expanded military action against ISIS -- but the key word there is'' considering.''
# Hypothesis: Two anti-war members of Congress consider supporting expanded military action.
# Golden Label: entailment

anti_war_members_premise = 3
anti_war_members_hypothesis = 2

# the hypothesis mentions the number of anti-war members considering support, which is also referenced in the premise
if anti_war_members_hypothesis > anti_war_members_premise:
    # check if the number of anti-war members in the hypothesis contradicts the number of anti-war members reported in the premise
    label = "contradiction"
elif anti_war_members_hypothesis < anti_war_members_premise:
    # if the number of anti-war members in the hypothesis is less than in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of anti-war members in the hypothesis equals the number in the premise, the label remains neutral
    label = "neutral"

print(label)

