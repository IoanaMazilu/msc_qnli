# Premise: A book store had 41.0 books in the bargin bin and they then sort out 2.0 books off the bin and sold 33.0 books.
# Hypothesis: 6.0 books would now be in the bin.
# Golden Label: entailment

initial_books_premise = 41.0
sorted_books_premise = 2.0
sold_books_premise = 33.0
remaining_books_hypothesis = 6.0

# the hypothesis refers to the number of remaining books in the bin, which is also mentioned in the premise
# compute the number of remaining books in the premise
remaining_books_premise = initial_books_premise - sorted_books_premise - sold_books_premise
if remaining_books_hypothesis != remaining_books_premise:
    # check if the number of remaining books in the hypothesis contradicts the number of remaining books from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

