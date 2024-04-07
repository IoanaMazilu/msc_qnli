# Premise: Jithin bought six books at an average price (arithmetic mean) of 20 $.
# Hypothesis: Jithin bought six books at an average price (arithmetic mean) of less than 60 $.
# Golden Label: entailment

books_bought_premise = 6
books_bought_hypothesis = 6
average_price_premise = 20
average_price_hypothesis = 60

# the hypothesis refers to the average price and number of books bought by Jithin which is also mentioned in the premise
if books_bought_premise != books_bought_hypothesis:
    # check if the number of books bought in the hypothesis contradicts the number of books bought in the premise
    label = "contradiction"
elif average_price_hypothesis <= average_price_premise:
    # check if the average price estimate in the hypothesis contradicts the average price in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

