words_typed_premise = 7
words_typed_hypothesis = 8
typing_rate = 4

# the hypothesis refers to the number of words James types and the rate at which he types, both mentioned in the premise
if words_typed_hypothesis <= words_typed_premise:
    # check if the number of words in the hypothesis contradicts the estimate of more than 'words_typed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words
    # any number of words greater than 'words_typed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
