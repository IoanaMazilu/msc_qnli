words_typed_premise = 7
words_typed_hypothesis = 8
words_per_minute = 4

# the hypothesis talks about the number of words James types, referenced also in the premise
if words_typed_hypothesis <= words_typed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'words_typed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'words_typed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
