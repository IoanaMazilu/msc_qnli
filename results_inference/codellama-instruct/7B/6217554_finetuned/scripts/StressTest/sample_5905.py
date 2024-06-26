# define variables for the quantities mentioned in the hypothesis
michael_cookies_hypothesis = 1/8
steve_cookies_hypothesis = 1/2
tyler_cookies_hypothesis = 150

# extract the quantities mentioned in the premise
michael_cookies_premise = 7/8
steve_cookies_premise = 1/2
tyler_cookies_premise = 150

# check if the hypothesis values contradict the premise ones
if michael_cookies_hypothesis!= michael_cookies_premise:
    label = "contradiction"
elif steve_cookies_hypothesis!= steve_cookies_premise:
    label = "contradiction"
elif tyler_cookies_hypothesis!= tyler_cookies_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
