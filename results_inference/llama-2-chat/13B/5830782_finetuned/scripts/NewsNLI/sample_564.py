poll_size_premise = 1005
redeem_rate_premise = 40
poll_size_hypothesis = None
redeem_rate_hypothesis = 40

# the hypothesis mentions the percentage of passengers who never redeem loyalty miles, which is also referenced in the premise
# however, the hypothesis does not specify the size of the survey, which is mentioned in the premise
if redeem_rate_hypothesis!= redeem_rate_premise:
    # check if the redemption rate in the hypothesis contradicts the redemption rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis redemption rate does not contradict the premise redemption rate, we can infer neutrality due to lack of survey size information
    label = "neutral"

print(label)
