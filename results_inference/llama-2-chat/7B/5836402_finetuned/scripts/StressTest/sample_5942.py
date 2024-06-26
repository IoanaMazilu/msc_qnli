gang_size_premise = 5
gang_size_hypothesis = 5

# the hypothesis refers to the number of gang members Mala has, mentioned in the premise
if gang_size_hypothesis <= gang_size_premise:
    # check if the hypothesis value contradicts the estimate of 'gang_size_premise'
    label = "contradiction"
else:
    # if the hypothesis value is greater than 'gang_size_premise', it is not possible to invite more gang members than what is stated in the premise
    # hence, the premise does not entail or contradict the hypothesis
    label = "neutral"

print(label)
