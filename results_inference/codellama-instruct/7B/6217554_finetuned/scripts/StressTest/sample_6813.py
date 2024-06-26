# the hypothesis refers to the percentage of students with cars at Morse, referenced also in the premise
if hypothesis_percentage < premise_percentage:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
