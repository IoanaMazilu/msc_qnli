white_socks_percentage_premise = 40
white_socks_percentage_hypothesis = 80

# the hypothesis refers to the proportion of white socks mentioned in the premise
if white_socks_percentage_premise >= white_socks_percentage_hypothesis:
    # check if the 'white_socks_percentage_premise' contradicts the estimate of less than 'white_socks_percentage_hypothesis'
    label = "contradiction"
elif white_socks_percentage_hypothesis > white_socks_percentage_premise:
    # check if the 'white_socks_percentage_hypothesis' is greater than 'white_socks_percentage_premise'
    label = "entailment"
else:
    # if neither condition applies, the relation can be considered neutral
    label = "neutral"

print(label)
