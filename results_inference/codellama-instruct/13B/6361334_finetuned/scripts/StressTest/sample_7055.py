amar_premise = 64
amar_hypothesis = 24
bhavan_premise = 36
bhavan_hypothesis = 36
chetan_premise = 44
chetan_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan and Chetan mentioned in the premise
if amar_hypothesis!= amar_premise:
    # check if the hypothesis value for Amar contradicts the score in the premise
    label = "contradiction"
elif bhavan_hypothesis!= bhavan_premise:
    # check if the hypothesis value for Bhavan contradicts the score in the premise
    label = "contradiction"
elif chetan_hypothesis!= chetan_premise:
    # check if the hypothesis value for Chetan contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
