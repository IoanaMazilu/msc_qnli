positive_integers_premise = 4
positive_integers_hypothesis = 3

# the hypothesis talks about the number of positive integers in a list, referenced also in the premise
if positive_integers_hypothesis >= positive_integers_premise:
    # check if the hypothesis value contradicts the estimate of less than 'positive_integers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of positive integers
    # any number of positive integers less than 'positive_integers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
