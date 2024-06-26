fraction_premise = 7/12
fraction_hypothesis = 7/12

# the hypothesis refers to the fraction of the sum of money T mentioned in the premise
if fraction_hypothesis <= fraction_premise:
    # check if the fraction in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the fraction in the hypothesis does not contradict the fraction in the premise, we can infer entailment
    label = "entailment"

print(label)
