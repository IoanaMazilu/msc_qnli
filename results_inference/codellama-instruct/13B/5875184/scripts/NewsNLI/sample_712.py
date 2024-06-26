premise_value = 100000
hypothesis_value = 100000

# the hypothesis mentions the value of the souvenirs, which is also mentioned in the premise
if hypothesis_value!= premise_value:
    # check if the value of the souvenirs in the hypothesis contradicts the value mentioned in the premise
    label = "contradiction"
else:
    # if the value of the souvenirs in the hypothesis does not contradict the value mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
