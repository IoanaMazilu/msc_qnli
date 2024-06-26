south_korean_crew_premise = 5
south_korean_crew_hypothesis = 5
philippine_crew_premise = 18
philippine_crew_hypothesis = 18

# the hypothesis refers to the nationalities of the crew members, which is also mentioned in the premise
if south_korean_crew_hypothesis!= south_korean_crew_premise:
    # check if the number of South Korean crew members in the hypothesis contradicts the number of South Korean crew members in the premise
    label = "contradiction"
elif philippine_crew_hypothesis!= philippine_crew_premise:
    # check if the number of Filipino crew members in the hypothesis contradicts the number of Filipino crew members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
