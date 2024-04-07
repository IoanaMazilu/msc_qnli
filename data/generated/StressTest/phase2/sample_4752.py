# Premise: Rita can knit a pair of socks in 3 days.
# Hypothesis: Rita can knit a pair of socks in less than 6 days.
# Golden Label: entailment

socks_knit_time_premise = 3
socks_knit_time_hypothesis = 6

# the hypothesis talks about the time Rita takes to knit a pair of socks, referenced also in the premise
if socks_knit_time_premise > socks_knit_time_hypothesis:
    # check if the knitting time in the premise contradicts the hypothesis claim of 'less than socks_knit_time_hypothesis' days
    label = "contradiction"
elif socks_knit_time_premise == socks_knit_time_hypothesis:
    # check if the knitting time in the premise contradicts the hypothesis claim of 'less than socks_knit_time_hypothesis' days
    label = "contradiction"
else:
    # if the knitting time in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

