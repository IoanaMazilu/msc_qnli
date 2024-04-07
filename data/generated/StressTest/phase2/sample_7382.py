# Premise: Jithin bought six books at an average price (arithmetic mean) of 20 $.
# Hypothesis: Jithin bought six books at an average price (arithmetic mean) of less than 20 $.
# Golden Label: contradiction

books_premise = 6
books_hypothesis = 6
average_price_premise = 20
average_price_hypothesis = 20

# the hypothesis refers to the number of books and their average price mentioned in the premise
if books_hypothesis != books_premise:
    # check if the number of books in the hypothesis contradicts the number of books mentioned in the premise
    label = "contradiction"
elif average_price_hypothesis >= average_price_premise:
    # check if the average book price in the hypothesis contradicts the average book price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

