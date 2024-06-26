cookies_eaten_michael_premise = 7/8
cookies_eaten_michael_hypothesis = 1/8
steve_cookies_eaten_premise = 1/2
steve_cookies_eaten_hypothesis = 1/2
tyler_extra_cookies_eaten_premise = 150
tyler_extra_cookies_eaten_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler mentioned in the premise
if cookies_eaten_michael_hypothesis >= cookies_eaten_michael_premise:
    # check if the estimate of 'cookies_eaten_michael_hypothesis' contradicts the number of cookies eaten by Michael in the premise
    label = "contradiction"
elif steve_cookies_eaten_hypothesis!= steve_cookies_eaten_premise:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif tyler_extra_cookies_eaten_hypothesis!= tyler_extra_cookies_eaten_premise:
    # check if the number of extra cookies eaten by Tyler in the hypothesis contradicts the number of extra cookies eaten by Tyler reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cookies eaten by Michael
    # any number of cookies less than 'cookies_eaten_michael_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
