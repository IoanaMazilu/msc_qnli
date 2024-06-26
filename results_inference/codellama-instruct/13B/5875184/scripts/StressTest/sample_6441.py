premise_grapes = 7
premise_mangoes = 9
hypothesis_grapes = 1
hypothesis_mangoes = 9

# the hypothesis refers to the number of kg of grapes and mangoes mentioned in the premise
if hypothesis_grapes <= premise_grapes:
    # check if the estimate of 'hypothesis_grapes' contradicts the number of kg of grapes in the premise
    label = "contradiction"
elif hypothesis_mangoes!= premise_mangoes:
    # check if the number of kg of mangoes in the hypothesis contradicts the number of kg of mangoes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
