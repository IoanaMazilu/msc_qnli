total_citizens_premise = 1005
loyalty_scheme_users_premise = 0.4
loyalty_scheme_users_hypothesis = 0.4

# the hypothesis mentions the percentage of people who never redeem miles, which is also mentioned in the premise
# however, the hypothesis does not specify the total number of people surveyed, which is specified in the premise
if loyalty_scheme_users_hypothesis!= loyalty_scheme_users_premise:
    # check if the percentage of people who never redeem miles in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer neutrality
    label = "neutral"

print(label)
