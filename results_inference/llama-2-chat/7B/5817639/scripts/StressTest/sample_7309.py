word_count_premise = 7
word_count_hypothesis = 8

# the hypothesis talks about the number of words James types, referenced also in the premise
if word_count_hypothesis <= word_count_premise:
    # check if the hypothesis value contradicts the estimate of more than 'word_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'word_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
