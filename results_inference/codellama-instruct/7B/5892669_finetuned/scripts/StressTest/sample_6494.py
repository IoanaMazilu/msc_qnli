percentage_given_back_premise = 3
percentage_given_back_hypothesis = 3

# the hypothesis refers to the percentage given back each month mentioned in the premise
if percentage_given_back_hypothesis >= percentage_given_back_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
