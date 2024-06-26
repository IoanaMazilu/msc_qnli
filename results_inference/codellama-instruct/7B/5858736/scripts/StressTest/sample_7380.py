book_price_premise = 20
book_price_hypothesis = 60

if book_price_hypothesis >= book_price_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
