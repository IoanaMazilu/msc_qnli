michael_cookies_premise = 7/8
michael_cookies_hypothesis = 1/8
steve_cookies_premise = 1/2
steve_cookies_hypothesis = 1/2
tyler_more_cookies_premise = 150
tyler_more_cookies_hypothesis = 150

# the hypothesis refers to the number of cookies eaten by Michael, Steve and Tyler, mentioned in the premise
if michael_cookies_hypothesis >= michael_cookies_premise:
    # check if the fraction of'michael_cookies_hypothesis' contradicts the fraction of Michael's cookies in the premise
    label = "contradiction"
elif steve_cookies_hypothesis!= steve_cookies_premise:
    # check if the fraction of'steve_cookies_hypothesis' contradicts the fraction of Steve's cookies in the premise
    label = "contradiction"
elif tyler_more_cookies_hypothesis!= tyler_more_cookies_premise:
    # check if the number of more cookies eaten by Tyler in the hypothesis contradicts the number of more cookies eaten by Tyler in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction of Michael's cookies
    # any fraction less than'michael_cookies_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
