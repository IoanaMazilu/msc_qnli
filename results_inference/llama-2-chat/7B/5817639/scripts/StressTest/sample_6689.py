book_copies_premise = 60
book_copies_hypothesis = 60
hardback_copies_premise = 10
hardback_copies_hypothesis = 10
paperback_copies_premise = 50
paperback_copies_hypothesis = 50

# the hypothesis talks about the number of copies of a book purchased by Bookman, referenced also in the premise
if book_copies_hypothesis <= book_copies_premise:
    # check if the hypothesis value contradicts the estimate of more than 'book_copies_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of copies purchased
    # any number of copies greater than 'book_copies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
