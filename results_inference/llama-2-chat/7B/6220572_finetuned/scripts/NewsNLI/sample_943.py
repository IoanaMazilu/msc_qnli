death_toll_hypothesis = 3
wounded_hypothesis = 260

# the hypothesis mentions the death toll and the number of wounded in the 2013 blasts, which are also referenced in the premise
if death_toll_hypothesis!= 3 or wounded_hypothesis!= 260:
    # check if the death toll or the number of wounded in the hypothesis contradicts the premise values
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
