pens_brought_premise = 150
pens_brought_hypothesis = 550

# the hypothesis refers to the number of pens brought home by Rihanna, mentioned also in the premise
if pens_brought_hypothesis <= pens_brought_premise:
    # check if the estimate of 'pens_brought_hypothesis' contradicts the number of pens brought home in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
