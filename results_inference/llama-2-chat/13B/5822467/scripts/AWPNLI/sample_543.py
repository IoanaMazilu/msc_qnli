books_premise = 54.0
books_given_away_premise = 23.0
books_hypothesis = 34.0

# compute the total number of books left in the premise
total_books_premise = books_premise - books_given_away_premise

if books_hypothesis > total_books_premise:
    # check if the number of books in the hypothesis contradicts the number of books from the premise
    label = "contradiction"
elif books_hypothesis < total_books_premise:
    # check if the number of books in the hypothesis is less than the number of books from the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
