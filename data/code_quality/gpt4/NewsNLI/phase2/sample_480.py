soldiers_premise = 20000
soldiers_hypothesis = 20000

# the hypothesis mentions the number of soldiers moved from the Afghanistan border to the Indian border, which is also mentioned in the premise
if soldiers_hypothesis != soldiers_premise:
    # check if the number of soldiers in the hypothesis contradicts the number of soldiers stated in the premise
    label = "contradiction"
else:
    # if the number of soldiers in the hypothesis does not contradict the number of soldiers in the premise, we can infer entailment
    label = "entailment"

print(label)
