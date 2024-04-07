# Premise: George's drawer has 7 loose black socks, 11 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has less than 8 loose black socks, 11 loose blue socks, and 8 loose white socks.
# Golden Label: entailment

black_socks_premise = 7
black_socks_hypothesis = 8
blue_socks_premise = 11
blue_socks_hypothesis = 11
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis talks about the number of each color of socks in George's drawer, which is also mentioned in the premise
if black_socks_hypothesis <= black_socks_premise:
    # check if the hypothesis value contradicts the premise value for black socks
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise or white_socks_hypothesis != white_socks_premise:
    # check if the hypothesis value contradicts the premise value for blue or white socks
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

