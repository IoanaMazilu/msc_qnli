crew_members_premise = 23
south_korean_crew_premise = 5
filipino_crew_premise = 18

south_korean_crew_hypothesis = 5
filipino_crew_hypothesis = 18

# the hypothesis mentions the total number of crew members, the number of South Korean crew members, and the number of Filipino crew members
# these are also mentioned in the premise
if crew_members_premise!= south_korean_crew_hypothesis + filipino_crew_hypothesis:
    # check if the total number of crew members in the hypothesis contradicts the sum of South Korean and Filipino crew members in the premise
    label = "contradiction"
elif south_korean_crew_premise!= south_korean_crew_hypothesis:
    # check if the number of South Korean crew members in the hypothesis contradicts the number of South Korean crew members in the premise
    label = "contradiction"
elif filipino_crew_premise!= filipino_crew_hypothesis:
    # check if the number of Filipino crew members in the hypothesis contradicts the number of Filipino crew members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
