books_bought_premise = 6
books_bought_hypothesis = 6
avg_price_premise = 20
avg_price_hypothesis = 20

# the hypothesis talks about the average price of books bought by Jithin, which is also mentioned in the premise
if avg_price_hypothesis <= avg_price_premise:
    # check if the hypothesis value contradicts the estimate of the average price in the premise
    label = "contradiction"
elif books_bought_hypothesis <= books_bought_premise:
    # check if the number of books bought in the hypothesis contradicts the number of books bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
