specific_socks_premise = 6
specific_socks_hypothesis = 2

# the hypothesis talks about the number of specific socks Barbara might wear, referenced also in the premise
if specific_socks_hypothesis >= specific_socks_premise:
    # check if the hypothesis value contradicts the estimate of not less than'specific_socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of specific socks
    # any number of socks less than'specific_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
