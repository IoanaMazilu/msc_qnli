books_premise = 5106.0
books_donated_premise = 1986.0
books_hypothesis = 3120.0

# compute the total number of books left in the school libraries
total_books_left_premise = books_premise - books_donated_premise

if books_hypothesis > total_books_left_premise:
    # check if the number of books left in the hypothesis contradicts the estimate of more than 'books_donated_premise'
    label = "contradiction"
elif books_hypothesis!= total_books_left_premise:
    # check if the number of books from the hypothesis contradicts the number of books in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)