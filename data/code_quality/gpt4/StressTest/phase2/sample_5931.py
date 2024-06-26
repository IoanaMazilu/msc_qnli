parts_premise = 5
parts_hypothesis = 4
equal_parts_premise = 6
equal_parts_hypothesis = 6
not_divisible_premise = 9
not_divisible_hypothesis = 9

# The hypothesis talks about the number of parts Antony can divide his herd into, referenced also in the premise
if parts_hypothesis >= parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'parts_premise'
    label = "contradiction"
elif equal_parts_hypothesis != equal_parts_premise or not_divisible_hypothesis != not_divisible_premise:
    # check if the number of equal parts or not divisible parts in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parts
    # any number of parts less than 'parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
