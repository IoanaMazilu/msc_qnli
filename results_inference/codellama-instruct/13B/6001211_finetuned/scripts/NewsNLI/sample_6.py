capsizations_premise = 2
capsizations_hypothesis = 3

# the hypothesis mentions the number of boat capsizations according to Jordan, which is also mentioned in the premise
if capsizations_hypothesis!= capsizations_premise:
    # check if the number of boat capsizations in the hypothesis contradicts the number of boat capsizations reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
