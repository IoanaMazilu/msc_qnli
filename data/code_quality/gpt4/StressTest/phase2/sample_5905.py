cookies_michael_premise = 7/8
cookies_michael_hypothesis = 1/8
cookies_steve_premise = 1/2
cookies_steve_hypothesis = 1/2
cookies_tyler_more_than_michael = 150 # this is the extra amount of cookies Tyler ate compared to Michael, in both the premise and hypothesis

# the hypothesis talks about the amount of cookies each person ate, referenced also in the premise
if cookies_michael_hypothesis >= cookies_michael_premise:
    # check if the amount of cookies Michael ate in the hypothesis contradicts the estimate of less than 'cookies_michael_premise'
    label = "contradiction"
elif cookies_steve_hypothesis != cookies_steve_premise:
    # check if the amount of cookies Steve ate in the hypothesis contradicts the amount reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
