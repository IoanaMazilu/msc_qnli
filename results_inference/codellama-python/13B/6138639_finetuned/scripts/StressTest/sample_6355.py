microtron_sale_premise = 76
microtron_sale_hypothesis = 36
dynaco_sale_premise = 48
dynaco_sale_hypothesis = 48
total_shares = 300
average_price = 40

# the hypothesis talks about the price of selling MicroTron and Dynaco stocks, referenced also in the premise
if microtron_sale_hypothesis >= microtron_sale_premise:
    # check if the hypothesis value contradicts the estimate of less than'microtron_sale_premise'
    label = "contradiction"
elif dynaco_sale_hypothesis!= dynaco_sale_premise:
    # check if the price of selling Dynaco stock in the hypothesis contradicts the price of selling Dynaco stock in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the price of selling MicroTron stock
    # any price of selling MicroTron stock less than'microtron_sale_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
