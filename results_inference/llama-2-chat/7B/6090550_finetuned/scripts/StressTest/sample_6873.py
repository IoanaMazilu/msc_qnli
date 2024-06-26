# the hypothesis is about the number of days Jhon works, which is also mentioned in the premise
if y <= 40:
    # check if the number of days in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the number of days in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
