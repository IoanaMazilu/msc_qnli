value_premise = 7/12
value_hypothesis = 4/12

# the hypothesis refers to the fraction of the sum of money Anup was asked to find, also mentioned in the premise
if value_premise <= value_hypothesis:
    # check if the fraction in the hypothesis contradicts the fraction in the premise
    label = "contradiction"
else:
    # if the fraction in the hypothesis does not contradict the fraction in the premise, we can infer entailment
    label = "entailment"

print(label)
