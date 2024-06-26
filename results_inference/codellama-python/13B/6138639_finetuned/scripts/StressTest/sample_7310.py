words_typed_premise = 8
words_typed_hypothesis = 8
words_per_minute = 4

# the hypothesis refers to the number of words James types, which is also mentioned in the premise
if words_typed_hypothesis >= words_typed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'words_typed_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of words
    # any number of words less than 'words_typed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
