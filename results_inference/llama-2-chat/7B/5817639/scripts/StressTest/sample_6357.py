nice_gift_premise = 5
nice_gift_hypothesis = 2

# the hypothesis talks about the number of baseball cards given, referenced also in the premise
if nice_gift_hypothesis <= nice_gift_premise:
    # check if the hypothesis value contradicts the estimate of 'nice_gift_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of baseball cards given
    # any number of baseball cards greater than 'nice_gift_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
