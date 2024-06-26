parts_premise = 4
parts_hypothesis = 5
equal_parts_premise = 6
equal_parts_hypothesis = 6
not_divisible_premise = 9
not_divisible_hypothesis = 9

# the hypothesis refers to the number of parts Antony can divide his herd into, mentioned in the premise
if parts_hypothesis <= parts_premise:
    # check if the number of parts in the hypothesis contradicts the estimate of more than 'parts_premise'
    label = "contradiction"
elif equal_parts_hypothesis!= equal_parts_premise or not_divisible_hypothesis!= not_divisible_premise:
    # check if the number of equal parts or the number that cannot be divided in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parts
    # any number of parts greater than 'parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
