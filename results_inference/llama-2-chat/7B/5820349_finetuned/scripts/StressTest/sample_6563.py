average_increase_premise = 2
average_increase_hypothesis = 2

# the hypothesis talks about the increase in average Jerry wants to achieve, which is also referenced in the premise
if average_increase_hypothesis <= average_increase_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_increase_premise'
    label = "contradiction"
else:
    # the premise gives an exact value for the increase in average
    # any increase greater than 'average_increase_premise' contradicts the premise
    label = "contradiction"

print(label)
