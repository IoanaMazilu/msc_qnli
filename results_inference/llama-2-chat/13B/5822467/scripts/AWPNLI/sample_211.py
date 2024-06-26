books_premise = 150.0 * 15.0
books_hypothesis = 2251.0

# check if the number of books in the hypothesis is greater than the number of books in the premise
if books_hypothesis > books_premise:
    label = "entailment"
elif books_hypothesis <= books_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
