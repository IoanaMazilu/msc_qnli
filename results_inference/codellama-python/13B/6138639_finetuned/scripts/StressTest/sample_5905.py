cookies_eaten_michael_premise = 7/8
cookies_eaten_michael_hypothesis = 1/8
cookies_eaten_steve_premise = 1/2
cookies_eaten_steve_hypothesis = 1/2
cookies_eaten_tyler_premise = 150
cookies_eaten_tyler_hypothesis = 150

# the hypothesis talks about the number of cookies eaten by Michael, Steve and Tyler, referenced also in the premise
if cookies_eaten_michael_hypothesis >= cookies_eaten_michael_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cookies_eaten_michael_premise'
    label = "contradiction"
elif cookies_eaten_steve_hypothesis!= cookies_eaten_steve_premise:
    # check if the number of cookies eaten by Steve in the hypothesis contradicts the number of cookies eaten by Steve reported in the premise
    label = "contradiction"
elif cookies_eaten_tyler_hypothesis!= cookies_eaten_tyler_premise:
    # check if the number of cookies eaten by Tyler in the hypothesis contradicts the number of cookies eaten by Tyler reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cookies eaten by Michael
    # any number of cookies less than 'cookies_eaten_michael_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
