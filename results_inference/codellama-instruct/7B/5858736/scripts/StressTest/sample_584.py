book_count_premise = 65
book_count_hypothesis = 65

# the hypothesis refers to the number of books bought by Rahim mentioned in the premise
if book_count_premise <= book_count_hypothesis:
    # check if the estimate of 'book_count_hypothesis' contradicts the number of books bought by Rahim in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of books bought by Rahim
    # any number of books greater than 'book_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
