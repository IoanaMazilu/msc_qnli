# Premise: George's drawer has 10 loose black socks, 15 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has less than 80 loose black socks, 15 loose blue socks, and 8 loose white socks.
# Golden Label: entailment

black_socks_premise = 10
black_socks_hypothesis = 80
blue_socks_premise = 15
blue_socks_hypothesis = 15
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis talks about the number of black, blue and white socks in George's drawer
if black_socks_hypothesis <= black_socks_premise:
    # check if the estimate of 'black_socks_hypothesis' contradicts the number of black socks in the premise
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise or white_socks_hypothesis != white_socks_premise:
    # check if the number of blue or white socks in the hypothesis contradicts the number of blue or white socks in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

