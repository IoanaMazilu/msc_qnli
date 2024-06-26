pubs_premise = 57000
pubs_hypothesis = 57000

# the hypothesis and the premise both mention the number of pubs in Britain
if pubs_hypothesis != pubs_premise:
    # check if the number of pubs in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of pubs in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
