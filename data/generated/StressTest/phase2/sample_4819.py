# Premise: George's drawer has less than 8 loose black socks, 11 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has 7 loose black socks, 11 loose blue socks, and 8 loose white socks.
# Golden Label: neutral

black_socks_premise = 8
black_socks_hypothesis = 7
blue_socks_premise = 11
blue_socks_hypothesis = 11
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis talks about the number of each color of socks in George's drawer, referenced also in the premise
if black_socks_hypothesis >= black_socks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'black_socks_premise'
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise:
    # check if the number of blue socks in the hypothesis contradicts the number of blue socks reported in the premise
    label = "contradiction"
elif white_socks_hypothesis != white_socks_premise:
    # check if the number of white socks in the hypothesis contradicts the number of white socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

