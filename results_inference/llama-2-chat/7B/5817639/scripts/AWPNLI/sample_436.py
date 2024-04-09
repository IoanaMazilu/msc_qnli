books_premise = float(5106.0)
books_hypothesis = float(3120.0)

# compare the number of books in the hypothesis with the number of books in the premise
if books_hypothesis >= books_premise:
    # if the number of books in the hypothesis does not contradict the number of books in the premise
    label = "entailment"
elif books_hypothesis - books_premise > 0:
    # if the number of books in the hypothesis is greater than the number of books in the premise
    label = "contradiction"
else:
    # if the number of books in the hypothesis is equal to the number of books in the premise
    label = "neutral"

print(label)
