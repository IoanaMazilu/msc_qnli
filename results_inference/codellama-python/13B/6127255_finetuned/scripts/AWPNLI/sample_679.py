bought_books_premise = 48.0
given_away_books_premise = 34.0
second_given_away_books_premise = 3.0
remaining_books_hypothesis = 12.0

# the hypothesis refers to the number of remaining coloring books, which are also mentioned in the premise
# compute the total number of coloring books in the premise
total_books_premise = bought_books_premise - given_away_books_premise - second_given_away_books_premise
if remaining_books_hypothesis!= total_books_premise:
    # check if the number of remaining coloring books in the hypothesis contradicts the number of remaining coloring books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
