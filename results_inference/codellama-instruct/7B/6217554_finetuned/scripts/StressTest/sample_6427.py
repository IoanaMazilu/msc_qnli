cookies_sold_premise = 750
cookies_sold_hypothesis = 450

if cookies_sold_hypothesis >= cookies_sold_premise:
    # check if the number of cookies sold in the hypothesis contradicts the estimate of less than 'cookies_sold_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cookies sold
    # any number of cookies sold less than 'cookies_sold_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
