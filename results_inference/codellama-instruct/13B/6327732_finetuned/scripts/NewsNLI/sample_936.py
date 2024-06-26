crew_south_korean_premise = 5
crew_south_korean_hypothesis = 5
crew_philippines_premise = 18
crew_philippines_hypothesis = 18

# the hypothesis mentions the number of South Korean and Filipino crew members, which are also mentioned in the premise
if crew_south_korean_hypothesis!= crew_south_korean_premise:
    # check if the number of South Korean crew members in the hypothesis contradicts the number of South Korean crew members in the premise
    label = "contradiction"
elif crew_philippines_hypothesis!= crew_philippines_premise:
    # check if the number of Filipino crew members in the hypothesis contradicts the number of Filipino crew members in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
