books_total = 5106.0
books_donated = 1986.0
books_left = 3120.0

# the hypothesis refers to the number of books left in the school libraries, which is also mentioned in the premise
if books_left!= (books_total - books_donated):
    # check if the number of books left in the hypothesis contradicts the number of books left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and calculations do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
