discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount percentage on the calculator mentioned in the premise
if discount_premise <= discount_hypothesis:
    # check if the discount percentage in the hypothesis contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # if the discount percentage in the hypothesis does not contradict the discount percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
