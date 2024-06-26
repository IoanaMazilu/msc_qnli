word_typing_premise = 8
word_typing_hypothesis = 8

# the hypothesis talks about the number of words typed by James at a rate of 4 words per minute
if word_typing_hypothesis <= word_typing_premise:
    # check if the hypothesis value contradicts the estimate of 'word_typing_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words typed
    # any number of words typed that is less than 'word_typing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
