sameer_share_premise = 6970
sameer_share_hypothesis = 1970

# the hypothesis talks about the share of Sameer in profit, referenced also in the premise
if sameer_share_hypothesis >= sameer_share_premise:
    # check if the hypothesis value contradicts the exact value of 'sameer_share_premise'
    label = "contradiction"
elif sameer_share_hypothesis < sameer_share_premise:
    # if the hypothesis value is less than 'sameer_share_premise', it does not contradict the premise
    # but it cannot be fully entailed from the premise because the premise suggests an exact amount
    label = "neutral"
else:
    # in any other case, we infer neutrality
    label = "neutral"

print(label)
