socks_premise = 5
shoes_premise = 3
socks_hypothesis = 2
shoes_hypothesis = 3

# the hypothesis talks about the number of socks and shoes owned by Tina, referenced also in the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the estimate of'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if shoes_hypothesis <= shoes_premise:
    # check if the hypothesis value contradicts the estimate of'shoes_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shoes
    # any number of shoes greater than'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
