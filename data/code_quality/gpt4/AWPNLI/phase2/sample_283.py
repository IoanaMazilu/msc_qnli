initial_books_premise = 34.0
given_away_books_premise = 3.0
bought_books_premise = 48.0
total_books_hypothesis = 78.0

# the hypothesis refers to the total number of books, which are also mentioned in the premise
# compute the total number of books in the premise
total_books_premise = initial_books_premise - given_away_books_premise + bought_books_premise
if total_books_hypothesis != total_books_premise:
    # check if the total number of books in the hypothesis contradicts the total number of books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
