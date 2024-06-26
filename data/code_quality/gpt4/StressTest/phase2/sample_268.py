black_socks_premise = 80
black_socks_hypothesis = 10
blue_socks_premise = 15
blue_socks_hypothesis = 15
white_socks_premise = 8
white_socks_hypothesis = 8

# the hypothesis talks about the number of each type of socks in George's drawer, referenced also in the premise
if black_socks_hypothesis > black_socks_premise:
    # check if the number of black socks in the hypothesis contradicts the estimate of less than 'black_socks_premise'
    label = "contradiction"
elif blue_socks_hypothesis != blue_socks_premise or white_socks_hypothesis != white_socks_premise:
    # check if the number of blue or white socks in the hypothesis contradicts the exact number of blue or white socks reported in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of black socks and exact numbers for the blue and white socks
    # the hypothesis is consistent with and can be fully and explicitly entailed from the premise
    label = "entailment"

print(label)
