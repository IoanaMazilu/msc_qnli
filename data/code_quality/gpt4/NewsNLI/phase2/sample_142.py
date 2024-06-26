soldiers_premise = 10000
police_premise = 8000
soldiers_hypothesis = 10000
police_hypothesis = 8000

# the hypothesis mentions the number of soldiers and police officers being deployed in France, which are also mentioned in the premise
if soldiers_hypothesis < soldiers_premise:
    # check if the number of soldiers in the hypothesis contradicts the number of soldiers in the premise
    label = "contradiction"
elif police_hypothesis < police_premise:
    # check if the number of police officers from the hypothesis contradicts the number of police officers in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
