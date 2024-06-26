average_increase_premise = 5
average_increase_hypothesis = 2

# The hypothesis talks about the increase in average when Robert's height is included, which is also mentioned in the premise
if average_increase_hypothesis >= average_increase_premise:
    # check if the hypothesized increase contradicts the premise's estimate of less than 'average_increase_premise'
    label = "contradiction"
elif average_increase_hypothesis < 0:
    # check if the hypothesized increase contradicts the premise's assertion of an increase
    label = "contradiction"
else:
    # the premise gives only an upper estimate for the increase
    # any increase less than 'average_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
