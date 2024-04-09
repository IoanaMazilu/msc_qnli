members_premise = 3
members_hypothesis = 2

# the hypothesis mentions the number of anti-war members of Congress considering supporting expanded military action, which is also referenced in the premise
if members_hypothesis!= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the number of members in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
