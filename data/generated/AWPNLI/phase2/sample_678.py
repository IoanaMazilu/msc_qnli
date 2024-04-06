# Premise: Faye bought 48.0 coloring books, and she gave away 34.0 of them and then gave away 3.0 more.
# Hypothesis: She would have 11.0 coloring books left.
# Golden Label: entailment

bought_books_premise = 48.0
gave_away_books_first_premise = 34.0
gave_away_books_second_premise = 3.0
left_books_hypothesis = 11.0

# the hypothesis refers to the number of coloring books left, which is also mentioned in the premise
# compute the total number of books left in the premise
left_books_premise = bought_books_premise - gave_away_books_first_premise - gave_away_books_second_premise
if left_books_hypothesis != left_books_premise:
    # check if the number of books left in the hypothesis contradicts the number of books left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

