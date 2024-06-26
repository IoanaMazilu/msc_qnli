south_korean_crew_premise = 5
filipino_crew_premise = 18
total_crew_hypothesis = 23
south_korean_crew_hypothesis = 5
filipino_crew_hypothesis = 18

# the hypothesis mentions the total number of crew and the number of South Korean and Filipino crew members, which are also mentioned in the premise
if total_crew_hypothesis!= (south_korean_crew_hypothesis + filipino_crew_hypothesis):
    # check if the total number of crew in the hypothesis contradicts the total number of crew reported in the premise
    label = "contradiction"
elif south_korean_crew_hypothesis!= south_korean_crew_premise:
    # check if the number of South Korean crew members from the hypothesis contradicts the number of South Korean crew members in the premise
    label = "contradiction"
elif filipino_crew_hypothesis!= filipino_crew_premise:
    # check if the number of Filipino crew members from the hypothesis contradicts the number of Filipino crew members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
