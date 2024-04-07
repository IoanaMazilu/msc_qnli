# Premise: Rita can knit a pair of socks in 3 days.
# Hypothesis: Rita can knit a pair of socks in less than 3 days.
# Golden Label: contradiction

socks_knitting_time_premise = 3
socks_knitting_time_hypothesis = 3

# the hypothesis refers to the time required to knit a pair of socks mentioned in the premise
if socks_knitting_time_hypothesis >= socks_knitting_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise gives the exact time for knitting a pair of socks
    # any time less than 'socks_knitting_time_premise' can not be explicitly entailed from the premise
    label = "neutral"

print(label)

