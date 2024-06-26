initial_peanuts_premise = 4
added_peanuts_premise = 12
initial_peanuts_hypothesis = 2
added_peanuts_hypothesis = 12

# the hypothesis talks about the initial quantity of peanuts in a box and the number of peanuts added by Mary
# these are the same quantities mentioned in the premise
if initial_peanuts_premise!= initial_peanuts_hypothesis or added_peanuts_premise!= added_peanuts_hypothesis:
    # check if the initial quantity of peanuts in the box or the number of peanuts added by Mary contradicts the premise
    label = "contradiction"
else:
    # the premise and hypothesis do not contradict each other, but they also don't entail each other
    label = "neutral"

print(label)
