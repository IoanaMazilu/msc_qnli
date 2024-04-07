# Premise: Tina has more than 1 socks and 3 pair of shoes.
# Hypothesis: Tina has 5 socks and 3 pair of shoes.
# Golden Label: neutral

socks_premise = 1
socks_hypothesis = 5
shoes_premise = 3
shoes_hypothesis = 3

# the hypothesis refers to the number of socks and shoes that Tina has, as mentioned in the premise
if socks_hypothesis <= socks_premise:
    # check if the number of socks in the hypothesis contradicts the estimate of more than 'socks_premise' socks
    label = "contradiction"
elif shoes_hypothesis != shoes_premise:
    # check if the number of pair of shoes in the hypothesis contradicts the number of pair of shoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks greater than 'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

