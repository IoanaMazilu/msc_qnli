south_korean_crew_premise = 5
philippine_crew_premise = 18
japanese_crew_hypothesis = 23
south_korean_crew_hypothesis = 5
philippine_crew_hypothesis = 18

# the hypothesis mentions the total number of crew and the number of South Korean and Filipino crew, which are also mentioned in the premise
if south_korean_crew_hypothesis!= south_korean_crew_premise:
    # check if the number of South Korean crew in the hypothesis contradicts the number of South Korean crew reported in the premise
    label = "contradiction"
elif philippine_crew_hypothesis!= philippine_crew_premise:
    # check if the number of Filipino crew from the hypothesis contradicts the number of Filipino crew in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
