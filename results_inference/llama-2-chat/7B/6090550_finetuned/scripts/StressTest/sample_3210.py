# the premise mentions the number of days he works at it
days_premise = 20
# the hypothesis mentions the number of days he works at it
days_hypothesis = 20
# the hypothesis talks about the number of days Rajesh finished it
days_rajesh = 30

# the hypothesis refers to the number of days he works at it and the number of days Rajesh finished it
if days_premise >= days_rajesh:
    # check if the number of days in the hypothesis contradicts the number of days in the premise
    label = "contradiction"
else:
    # if the number of days in the hypothesis does not contradict the number of days in the premise, we can infer entailment
    label = "entailment"

print(label)
