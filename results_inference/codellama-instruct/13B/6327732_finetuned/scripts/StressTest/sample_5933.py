herd_size_premise = 5
herd_size_hypothesis = 6

# the hypothesis refers to the number of equal parts that Antony can divide his herd into
if herd_size_hypothesis <= herd_size_premise:
    # check if the hypothesis value contradicts the estimate of more than 'herd_size_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of equal parts that Antony can divide his herd into
    # any number of equal parts greater than 'herd_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
