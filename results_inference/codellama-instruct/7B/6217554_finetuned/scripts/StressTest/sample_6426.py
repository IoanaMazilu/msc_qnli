cookies_sold_premise = 450
cookies_sold_hypothesis = 750

if cookies_sold_hypothesis <= cookies_sold_premise:
    # check if the hypothesis value contradicts the estimate of more than 'cookies_sold_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cookies sold
    # any number of cookies sold greater than 'cookies_sold_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
