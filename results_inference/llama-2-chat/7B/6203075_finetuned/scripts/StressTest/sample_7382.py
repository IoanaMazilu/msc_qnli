books_premise = 6
books_hypothesis = 6
price_premise = 20
price_hypothesis = 20

# the hypothesis refers to the number of books and their average price mentioned in the premise
if books_hypothesis!= books_premise:
    # check if the number of books in the hypothesis contradicts the number of books in the premise
    label = "contradiction"
elif price_hypothesis >= price_premise:
    # check if the average price in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
