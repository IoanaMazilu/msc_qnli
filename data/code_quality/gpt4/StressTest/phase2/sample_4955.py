black_socks_premise = 10
black_socks_hypothesis = 10
blue_socks_premise = 14
blue_socks_hypothesis = 14
white_socks_premise = 8
white_socks_hypothesis = 8

# The hypothesis refers to the number of each color of socks that George has in his drawer as mentioned in the premise
if black_socks_premise > black_socks_hypothesis:
    # Check if the count of 'black_socks_hypothesis' contradicts the number of black socks in the premise
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise:
    # Check if the number of blue socks in the hypothesis contradicts the number of blue socks reported in the premise
    label = "contradiction"
elif white_socks_hypothesis != white_socks_premise:
    # Check if the number of white socks in the hypothesis contradicts the number of white socks reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
