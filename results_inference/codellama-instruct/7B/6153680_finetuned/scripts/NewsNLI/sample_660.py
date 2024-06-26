pubs_remaining_premise = 57000
pubs_remaining_hypothesis = 57000

# the hypothesis mentions the number of pubs remaining in Britain, which is also mentioned in the premise
if pubs_remaining_hypothesis!= pubs_remaining_premise:
    # check if the number of pubs remaining in the hypothesis contradicts the number of pubs remaining in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values match, we can infer entailment
    label = "entailment"

print(label)
