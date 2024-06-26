cookies_michael_premise = 7/8
cookies_michael_hypothesis = 1/8
cookies_steve_premise = 1/2
cookies_steve_hypothesis = 1/2
cookies_tyler_premise = 150
cookies_tyler_hypothesis = 150

# the hypothesis refers to the amount of cookies Michael ate, Steve ate and Tyler ate
if cookies_michael_hypothesis >= cookies_michael_premise:
    # check if the amount of cookies Michael ate in the hypothesis contradicts the estimate of less than 'cookies_michael_premise'
    label = "contradiction"
elif cookies_steve_hypothesis!= cookies_steve_premise or cookies_tyler_hypothesis!= cookies_tyler_premise:
    # check if the amount of cookies Steve or Tyler ate in the hypothesis contradicts the amount of cookies they ate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
