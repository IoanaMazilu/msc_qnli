words_typed_premise = 8
words_typed_hypothesis = 7

# the hypothesis talks about the number of words typed by James, which is also referred to in the premise
if words_typed_hypothesis <= words_typed_premise:
    # check if the hypothesis value contradicts the estimate of 'words_typed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words typed
    # any number of words typed greater than 'words_typed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
