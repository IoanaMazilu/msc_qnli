antiwar_members_premise = 3
antiwar_members_hypothesis = 2

# the hypothesis mentions the number of anti-war members in Congress, which is also referenced in the premise
# however, the hypothesis does not mention the word "considering" which is mentioned in the premise
if antiwar_members_hypothesis!= antiwar_members_premise:
    # check if the number of anti-war members in the hypothesis contradicts the number of anti-war members in the premise
    label = "contradiction"
else:
    # if the number of anti-war members in the hypothesis does not contradict the number of anti-war members in the premise, we can infer neutrality
    label = "neutral"

print(label)
