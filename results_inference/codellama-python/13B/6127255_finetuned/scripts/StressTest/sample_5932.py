parts_premise = 4
parts_hypothesis = 5
parts_premise_equal = 6
parts_hypothesis_equal = 6
parts_premise_not_equal = 9
parts_hypothesis_not_equal = 9

# the hypothesis talks about the number of parts Antony can divide his herd into, referenced also in the premise
if parts_hypothesis <= parts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'parts_premise'
    label = "contradiction"
elif parts_hypothesis_equal!= parts_premise_equal or parts_hypothesis_not_equal!= parts_premise_not_equal:
    # check if the number of parts in the hypothesis contradicts the number of parts reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of parts
    # any number of parts greater than 'parts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
