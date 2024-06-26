michael_cookies_premise = 1/8
michael_cookies_hypothesis = 1/8

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if michael_cookies_hypothesis <= michael_cookies_premise:
    # check if the estimate of'michael_cookies_hypothesis' contradicts the number of cookie eaten by Michael in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
