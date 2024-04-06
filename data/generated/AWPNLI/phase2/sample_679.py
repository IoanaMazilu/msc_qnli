# Premise: Faye bought 48.0 coloring books, and she gave away 34.0 of them and then gave away 3.0 more.
# Hypothesis: She would have 12.0 coloring books left.
# Golden Label: contradiction

bought_books_premise = 48.0
first_gave_books_premise = 34.0
second_gave_books_premise = 3.0
remaining_books_hypothesis = 12.0

# the hypothesis refers to the number of coloring books left, which are also mentioned in the premise
# calculate the total number of books left according to the premise
remaining_books_premise = bought_books_premise - first_gave_books_premise - second_gave_books_premise
if remaining_books_hypothesis != remaining_books_premise:
    # check if the number of remaining books in the hypothesis contradicts the number of remaining books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"  

print(label)

