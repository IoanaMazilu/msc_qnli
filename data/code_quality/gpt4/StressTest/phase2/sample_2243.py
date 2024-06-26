white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis speaks about the percentage of white socks in a shop, which is also referenced in the premise
if white_socks_hypothesis == white_socks_premise:
    # check if the percentage of white socks in the hypothesis is the same as in the premise
    label = "entailment"
else:
    # if the percentage of white socks in the hypothesis is not the same as in the premise, it is a contradiction
    label = "contradiction"

print(label)
