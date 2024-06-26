t_shirts_returned_premise = 4
t_shirts_returned_hypothesis = 5
average_price_remaining_premise = 0
average_price_remaining_hypothesis = 0

# the hypothesis talks about the number of returned t-shirts and the average price of the remaining ones, referenced also in the premise
if t_shirts_returned_hypothesis <= t_shirts_returned_premise:
    # check if the hypothesis value contradicts the estimate of more than 't_shirts_returned_premise'
    label = "contradiction"
elif average_price_remaining_hypothesis!= average_price_remaining_premise:
    # check if the average price of the remaining t-shirts in the hypothesis contradicts the average price of the remaining t-shirts reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of returned t-shirts
    # any number of returned t-shirts greater than 't_shirts_returned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
