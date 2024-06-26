# the premise and hypothesis both deal with the denominations of US saving bonds
# the premise specifies $50 and $100 as the only denominations
# the hypothesis specifies $70 and $100 as the only denominations

if denomination_premise!= denomination_hypothesis:
    # check if the denominations in the hypothesis contradict the denominations in the premise
    label = "contradiction"
else:
    # if the denominations are the same, we can infer entailment
    label = "entailment"

print(label)
