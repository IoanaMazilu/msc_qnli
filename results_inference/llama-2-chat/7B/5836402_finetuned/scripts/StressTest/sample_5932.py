equal_parts_premise = 4
equal_parts_hypothesis = 5
equal_parts_hypothesis = 6
equal_parts_hypothesis = 9

# the hypothesis talks about the number of equal parts Antony can divide his herd into, referenced also in the premise
if equal_parts_hypothesis <= equal_parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'equal_parts_premise'
    label = "contradiction"
elif equal_parts_hypothesis == equal_parts_premise:
    # check if the number of equal parts in the hypothesis matches the number of equal parts in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of equal parts
    # any number of equal parts greater than 'equal_parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
