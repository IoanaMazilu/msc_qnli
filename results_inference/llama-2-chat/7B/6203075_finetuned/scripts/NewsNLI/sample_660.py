pubs_premise = 57000
pubs_hypothesis = 57000

# the hypothesis mentions the number of pubs in Britain, which is also mentioned in the premise
if pubs_hypothesis!= pubs_premise:
    # check if the number of pubs in the hypothesis contradicts the number of pubs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
