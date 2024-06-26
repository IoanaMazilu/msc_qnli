words_premise = 7
words_hypothesis = 8
rate_premise = 4
rate_hypothesis = 4

# the hypothesis refers to the number of words James types per minute, which is also mentioned in the premise
if words_hypothesis <= words_premise:
    # check if the number of words in the hypothesis contradicts the premise's estimate of more than 'words_premise'
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the typing rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'words_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
