# Premise: Mrs. Hilt reads 5.0 books a day.
# Hypothesis: She read 16.0 books.
# Golden Label: contradiction

books_per_day_premise = 5.0
total_books_hypothesis = 16.0

# the hypothesis refers to the total number of books read, which could be inferred from the premise
# assuming that she reads books every day, the minimum number of books she could read in one day is 'books_per_day_premise'
if total_books_hypothesis < books_per_day_premise:
    # check if the total number of books in the hypothesis contradicts the minimum number of books she could read in a day from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

