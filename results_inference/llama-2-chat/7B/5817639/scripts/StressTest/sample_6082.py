# Premise: If Rahul finds that he is less than 62 th from the right in a line of boys and 4 th from the left, how many boys should be added to the line such that there are 28 boys in the line?
less_than_62_th_premise = 62
less_than_62_th_hypothesis = 12

# the hypothesis talks about the position of Rahul in a line of boys, referenced also in the premise
if less_than_62_th_hypothesis <= less_than_62_th_premise:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_62_th_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the position of Rahul in the line
    # any position of Rahul less than 'less_than_62_th_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
