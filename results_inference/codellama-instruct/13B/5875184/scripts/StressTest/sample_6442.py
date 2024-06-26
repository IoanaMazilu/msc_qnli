premise_grapes = 1
premise_mangoes = 9
hypothesis_grapes = 7
hypothesis_mangoes = 9

# the hypothesis refers to the number of kg of grapes and mangoes mentioned in the premise
if hypothesis_grapes <= premise_grapes and hypothesis_mangoes <= premise_mangoes:
    # check if the estimate of 'hypothesis_grapes' and 'hypothesis_mangoes' contradicts the number of kg of grapes and mangoes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of grapes and mangoes
    # any number of kg of grapes and mangoes greater than 'premise_grapes' and 'premise_mangoes' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
