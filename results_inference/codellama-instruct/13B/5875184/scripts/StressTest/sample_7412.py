premise_kg = 27
premise_rs = 100
hypothesis_kg = 77
hypothesis_rs = 100

# the hypothesis refers to the total amount of butter mixed by Raman
if hypothesis_kg > premise_kg:
    # check if the hypothesis value contradicts the estimate of 'premise_kg'
    label = "contradiction"
elif hypothesis_rs!= premise_rs:
    # check if the price mentioned in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
