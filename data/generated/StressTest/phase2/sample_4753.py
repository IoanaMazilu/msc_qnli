# Premise: Rita can knit a pair of socks in less than 6 days.
# Hypothesis: Rita can knit a pair of socks in 3 days.
# Golden Label: neutral

socks_knitting_time_premise = 6
socks_knitting_time_hypothesis = 3

# The hypothesis talks about the time Rita takes to knit a pair of socks, referenced also in the premise
if socks_knitting_time_hypothesis >= socks_knitting_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'socks_knitting_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time to knit socks
    # any time less than 'socks_knitting_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

