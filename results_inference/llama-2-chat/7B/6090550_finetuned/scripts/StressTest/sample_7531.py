positive_ints_premise = 4
positive_ints_hypothesis = 3

# the hypothesis talks about the number of positive integers in the list, referenced also in the premise
if positive_ints_hypothesis >= positive_ints_premise:
    # check if the hypothesis value contradicts the premise statement of less than 'positive_ints_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of positive integers
    # any number of positive integers less than 'positive_ints_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
