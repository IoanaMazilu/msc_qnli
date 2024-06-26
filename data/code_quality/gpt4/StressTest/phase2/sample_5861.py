chocolates_premise = 15
chocolates_hypothesis = 15

# the hypothesis refers to the number of chocolates that Zada has to distribute among her children, mentioned in the premise
if chocolates_hypothesis >= chocolates_premise:
    # check if the hypothesis value contradicts the number of chocolates in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
