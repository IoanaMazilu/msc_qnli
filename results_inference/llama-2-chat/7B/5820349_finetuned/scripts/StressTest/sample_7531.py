integers_premise = 4
integers_hypothesis = 3

# the hypothesis refers to the number of positive integers in the list L mentioned in the premise
if integers_hypothesis >= integers_premise:
    # check if the number of integers in the hypothesis contradicts the estimate of less than 'integers_premise'
    label = "contradiction"
elif integers_hypothesis < integers_premise:
    # the premise gives only an estimate for the number of integers
    # any number of integers less than 'integers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
