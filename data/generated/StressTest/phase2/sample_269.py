# Premise: George's drawer has 10 loose black socks, 15 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has 50 loose black socks, 15 loose blue socks, and 8 loose white socks.
# Golden Label: contradiction

black_socks_premise = 10
black_socks_hypothesis = 50
blue_socks_premise = 15
blue_socks_hypothesis = 15
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis refers to the number of each color of socks mentioned in the premise
if black_socks_hypothesis != black_socks_premise:
    # check if the number of black socks in the hypothesis contradicts the number of black socks reported in the premise
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

