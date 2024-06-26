michael_cookies_premise = 1/8
michael_cookies_hypothesis = 7/8
steve_cookies_premise = 1/2
steve_cookies_hypothesis = 1/2
tyler_extra_cookies_premise = 150
tyler_extra_cookies_hypothesis = 150

# the hypothesis refers to the amount of cookies each character ate in the premise
if michael_cookies_hypothesis <= michael_cookies_premise:
    # check if the estimate of 'michael_cookies_hypothesis' contradicts the amount of cookies Michael ate in the premise
    label = "contradiction"
elif steve_cookies_hypothesis != steve_cookies_premise:
    # check if the amount of cookies Steve ate in the hypothesis contradicts the amount Steve ate in the premise
    label = "contradiction"
elif tyler_extra_cookies_hypothesis != tyler_extra_cookies_premise:
    # check if the amount of extra cookies Tyler ate in the hypothesis contradicts the amount of extra cookies Tyler ate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
