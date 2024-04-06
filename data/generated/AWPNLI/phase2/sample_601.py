# Premise: There are 38.0 books on the shelf and Marta takes 10.0 books off the shelf.
# Hypothesis: 26.0 books are on the shelf now.
# Golden Label: contradiction

books_premise = 38.0
taken_books_premise = 10.0
books_hypothesis = 26.0

# the hypothesis refers to the number of books on the shelf, which is also referenced in the premise
# find the remaining number of books on the shelf from the premise 
remaining_books_premise = books_premise - taken_books_premise
if remaining_books_premise != books_hypothesis:
    # check if the number of books from the hypothesis contradicts the remaining number of books in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)

