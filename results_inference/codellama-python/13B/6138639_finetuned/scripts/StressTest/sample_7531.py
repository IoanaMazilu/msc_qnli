integers_premise = 4
integers_hypothesis = 3

# the hypothesis talks about the number of integers in a list, referenced also in the premise
if integers_hypothesis >= integers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'integers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of integers
    # any number of integers less than 'integers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
