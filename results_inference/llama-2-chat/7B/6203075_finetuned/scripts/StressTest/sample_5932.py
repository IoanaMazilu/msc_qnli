# the hypothesis refers to the number of equal parts Antony can divide his herd into
equal_parts_hypothesis = 5
equal_parts_premise = 6
equal_parts_max = 9

# the premise states that Antony can divide his herd into more than 4 equal parts and also to 6 equal parts, but not to 9 equal parts
if equal_parts_hypothesis >= 4:
    # check if the number of equal parts in the hypothesis contradicts the premise
    if equal_parts_hypothesis!= 6:
        label = "contradiction"
elif equal_parts_hypothesis > equal_parts_max:
    # check if the number of equal parts in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the number of equal parts in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
