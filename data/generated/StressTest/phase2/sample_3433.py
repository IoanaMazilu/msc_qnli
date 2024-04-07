# Premise: George's drawer has less than 40 loose black socks, 13 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has 10 loose black socks, 13 loose blue socks, and 8 loose white socks.
# Golden Label: neutral

black_socks_premise = 40
black_socks_hypothesis = 10
blue_socks_premise = 13
blue_socks_hypothesis = 13
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis talks about the number of each color of socks in George's drawer
if black_socks_hypothesis >= black_socks_premise:
    # check if the number of black socks in the hypothesis contradicts the estimate of less than 'black_socks_premise'
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise:
    # check if the number of blue socks in the hypothesis contradicts the number of blue socks reported in the premise
    label = "contradiction"
elif white_socks_hypothesis != white_socks_premise:
    # check if the number of white socks in the hypothesis contradicts the number of white socks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

