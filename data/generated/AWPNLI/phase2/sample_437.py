# Premise: There are 5106.0 books in the Oak Grove school libraries and they donated 1986.0 to the public ibrary.
# Hypothesis: 3124.0 books are left in the school libraries.
# Golden Label: contradiction

total_books_premise = 5106.0
donated_books_premise = 1986.0
remaining_books_hypothesis = 3124.0

# the hypothesis refers to the number of remaining books in the school libraries, which can be computed from the premise
# compute the remaining number of books in the premise
remaining_books_premise = total_books_premise - donated_books_premise
if remaining_books_hypothesis != remaining_books_premise:
    # check if the number of remaining books in the hypothesis contradicts the number of remaining books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

