ratio_premise = [7, 3, 2]
ratio_hypothesis = [8, 3, 2]

# the hypothesis talks about the ratio of questions submitted by Rajat, Vikas and Abhishek
# the premise gives the ratio in the form of a list
if ratio_hypothesis[0] <= ratio_premise[0]:
    # check if the hypothesis value contradicts the estimate of less than 'ratio_premise[0]'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio
    # any ratio greater than 'ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
