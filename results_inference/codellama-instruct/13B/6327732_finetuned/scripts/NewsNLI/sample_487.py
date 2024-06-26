# define variables for the premise and hypothesis
premise = "Three of the key anti-war members of Congress are considering supporting expanded military action against ISIS -- but the key word there is'' considering.''"
hypothesis = "Two anti-war members of Congress consider supporting expanded military action."

# extract the number of anti-war members of Congress from the premise
anti_war_members_premise = 3

# extract the number of anti-war members of Congress from the hypothesis
anti_war_members_hypothesis = 2

# check if the number of anti-war members in the hypothesis contradicts the number in the premise
if anti_war_members_hypothesis!= anti_war_members_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
