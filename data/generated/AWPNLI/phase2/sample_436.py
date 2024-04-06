# Premise: There are 5106.0 books in the Oak Grove school libraries and they donated 1986.0 to the public ibrary.
# Hypothesis: 3120.0 books are left in the school libraries.
# Golden Label: entailment

books_premise = 5106.0
donated_books_premise = 1986.0
left_books_hypothesis = 3120.0

# the hypothesis refers to the number of left books, which are also mentioned in the premise
# compute the number of books left in the premise
left_books_premise = books_premise - donated_books_premise
if left_books_hypothesis != left_books_premise:
    # check if the number of left books in the hypothesis contradicts the number of left books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

