# the hypothesis refers to the number of fishes caught by Sony and Johnny
y_entailment = 60

# the hypothesis value is not mentioned in the premise
if y_entailment!= 40:
    # check if the number of fishes caught in the hypothesis contradicts the number of fishes caught in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
