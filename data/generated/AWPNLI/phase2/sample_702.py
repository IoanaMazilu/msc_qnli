# Premise: Vincent bought 10.0 books about animals, 1.0 book about outer space, and 3.0 books about trains and he paid $16.0 for all the books combined.
# Hypothesis: The average price for 1.0 book is 1.14285714286.
# Golden Label: entailment

books_animals_premise = 10.0
books_space_premise = 1.0
books_trains_premise = 3.0
total_payment_premise = 16.0
average_price_hypothesis = 1.14285714286

# the hypothesis refers to the average price of the books, which is also mentioned in the premise
# compute the total number of books and the average price per book in the premise
total_books_premise = books_animals_premise + books_space_premise + books_trains_premise
average_price_premise = total_payment_premise / total_books_premise
if average_price_hypothesis != average_price_premise:
    # check if the average price per book in the hypothesis contradicts the average price per book from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

