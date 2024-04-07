# Premise: An investor can sell her MicroTron stock for 36 $per share and her Dynaco stock for 56 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Hypothesis: An investor can sell her MicroTron stock for 46 $per share and her Dynaco stock for 56 $per share, If she sells 300 shares altogether, some of each stock, at an average price per share of 40 $, how many shares of Dynaco stock has she sold?
# Golden Label: contradiction

microtron_price_premise = 36
dynaco_price_premise = 56
shares_sold_premise = 300
average_price_premise = 40

microtron_price_hypothesis = 46
dynaco_price_hypothesis = 56
shares_sold_hypothesis = 300
average_price_hypothesis = 40

# the hypothesis refers to the price per share of MicroTron and Dynaco stocks, number of shares sold and average price per share mentioned in the premise
if microtron_price_hypothesis != microtron_price_premise:
    # check if the price per share of MicroTron in the hypothesis contradicts the price per share of MicroTron in the premise
    label = "contradiction"
elif dynaco_price_hypothesis != dynaco_price_premise or shares_sold_hypothesis != shares_sold_premise or average_price_hypothesis != average_price_premise:
    # check if the price per share of Dynaco, number of shares sold or average price per share in the hypothesis contradicts the respective values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

