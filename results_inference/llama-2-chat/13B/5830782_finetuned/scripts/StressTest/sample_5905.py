cookies_michael_premise = 7/8
cookies_michael_hypothesis = 1/8
cookies_steve_premise = 1/2
cookies_steve_hypothesis = 1/2
cookies_tyler_more_than_michael = 150

# the hypothesis refers to the amount of cookies eaten by Michael, Steve and Tyler
if cookies_michael_hypothesis >= cookies_michael_premise:
    # check if the amount of cookies Michael ate in the hypothesis contradicts the premise
    label = "contradiction"
elif cookies_steve_hypothesis!= cookies_steve_premise:
    # check if the amount of cookies Steve ate in the hypothesis contradicts the premise
    label = "contradiction"
elif cookies_tyler_more_than_michael!= cookies_tyler_more_than_michael:
    # check if the amount of cookies Tyler ate in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
