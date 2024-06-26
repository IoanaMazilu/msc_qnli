typed_words_premise = 7
typed_words_hypothesis = 8
typing_rate_premise = 4
typing_rate_hypothesis = 4

# the hypothesis refers to the number of words typed by James, which is also mentioned in the premise
if typed_words_hypothesis <= typed_words_premise:
    # check if the hypothesis value contradicts the estimate of more than 'typed_words_premise'
    label = "contradiction"
elif typing_rate_hypothesis!= typing_rate_premise:
    # check if the typing rate in the hypothesis contradicts the typing rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'typed_words_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
