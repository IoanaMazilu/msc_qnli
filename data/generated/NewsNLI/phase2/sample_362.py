# Premise: Among those charged are 158 members and associates of MS-13, with 105 others allegedly belonging to other gangs.
# Hypothesis: Gang sweep nabs 158 members and associates of notorious MS-13 gang, among others.
# Golden Label: entailment

ms13_members_premise = 158
ms13_members_hypothesis = 158
other_gang_members_premise = 105

# the hypothesis mentions the number of MS-13 members, which is also mentioned in the premise
# however, the hypothesis does not specify the number of members belonging to other gangs
if ms13_members_hypothesis != ms13_members_premise:
    # check if the number of MS-13 members in the hypothesis contradicts the number of MS-13 members reported in the premise
    label = "contradiction"
else:
    # if the number of MS-13 members in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

