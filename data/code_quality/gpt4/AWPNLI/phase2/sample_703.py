books_animals_premise = 10.0
book_space_premise = 1.0
books_trains_premise = 3.0
total_price_premise = 16.0
average_price_hypothesis = 4.6

# the hypothesis refers to the average price per book, which can be computed from the premise
# compute the total number of books in the premise
total_books_premise = books_animals_premise + book_space_premise + books_trains_premise

# compute the average price per book from the premise
average_price_premise = total_price_premise / total_books_premise

if average_price_hypothesis != average_price_premise:
    # check if the average price per book in the hypothesis contradicts the average price per book from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
