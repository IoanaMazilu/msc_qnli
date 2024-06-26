books_claire_premise = 1
books_claire_hypothesis = 3

# The hypothesis mentions a specific number of books that Claire has, which is also referenced in the premise
if books_claire_hypothesis <= books_claire_premise:
    # Check if the number of books in the hypothesis contradicts the 'more than 1 book' estimate given in the premise
    label = "contradiction"
else:
    # The premise provides only an estimate for the number of books Claire has
    # Any number of books greater than 'books_claire_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
