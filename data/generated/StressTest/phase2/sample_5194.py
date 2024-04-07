# Premise: George's drawer has less than 70 loose black socks, 12 loose blue socks, and 8 loose white socks.
# Hypothesis: George's drawer has 10 loose black socks, 12 loose blue socks, and 8 loose white socks.
# Golden Label: neutral

black_socks_premise = 70
black_socks_hypothesis = 10
blue_socks_premise = 12
blue_socks_hypothesis = 12
white_socks_premise = 8
white_socks_hypothesis = 8

# The hypothesis refers to the number of black, blue and white socks in George's drawer, mentioned in the premise
if black_socks_hypothesis > black_socks_premise:
    # Check if the number of 'black_socks_hypothesis' contradicts the estimate of less than 'black_socks_premise'
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise:
    # Check if the number of 'blue_socks_hypothesis' contradicts the exact number of blue socks in the premise
    label = "contradiction"
elif white_socks_hypothesis != white_socks_premise:
    # Check if the number of 'white_socks_hypothesis' contradicts the exact number of white socks in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

