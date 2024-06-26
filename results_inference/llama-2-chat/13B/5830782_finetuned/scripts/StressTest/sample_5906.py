michael_cookies_premise = 1/8
michael_cookies_hypothesis = 1/8
steve_cookies_premise = 1/2
steve_cookies_hypothesis = 1/2
tyler_cookies_difference_premise = 150
tyler_cookies_difference_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if michael_cookies_hypothesis <= michael_cookies_premise:
    # check if the estimate of'michael_cookies_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif steve_cookies_hypothesis!= steve_cookies_premise:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif tyler_cookies_difference_hypothesis!= tyler_cookies_difference_premise:
    # check if the difference in the number of cookies eaten by Tyler and Michael in the hypothesis contradicts the same difference reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
