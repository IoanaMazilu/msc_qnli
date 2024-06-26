michael_cookies_premise = 1/8
michael_cookies_hypothesis = 1/8
steve_cookies_premise = 1/2
steve_cookies_hypothesis = 1/2
tyler_cookies_premise = 150
tyler_cookies_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if michael_cookies_premise >= michael_cookies_hypothesis:
    # check if the estimate of'michael_cookies_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif steve_cookies_premise!= steve_cookies_hypothesis:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif tyler_cookies_premise!= tyler_cookies_hypothesis:
    # check if the number of cookies eaten by Tyler in the hypothesis contradicts the number of cookies eaten by Tyler reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)