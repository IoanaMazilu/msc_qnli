socks_premise = 5
shoes_premise = 3
socks_hypothesis = 1
shoes_hypothesis = 3

# the hypothesis talks about the number of socks and shoes in the same way as the premise
if socks_hypothesis <= socks_premise:
    # check if the hypothesis value contradicts the estimate of more than'socks_premise'
    label = "contradiction"
elif shoes_hypothesis!= shoes_premise:
    # check if the number of shoes in the hypothesis contradicts the number of shoes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks and shoes
    # any number of socks and shoes greater than'socks_premise' and'shoes_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
