countries_premise = 3
denmark_index_premise = 0
sweden_index_premise = 1
britain_index_premise = 2

# the hypothesis talks about Sweden adopting the single European currency in 1999
# the premise mentions Sweden and Britain opting not to join the euro currency system in its initial phase
# Denmark is not mentioned in the premise, so it cannot be inferred from the hypothesis
if denmark_index_premise!= 0:
    # check if the index of Denmark in the premise contradicts the hypothesis
    label = "contradiction"
elif sweden_index_premise!= 1 or britain_index_premise!= 2:
    # check if the indices of Sweden and Britain in the premise contradict the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
