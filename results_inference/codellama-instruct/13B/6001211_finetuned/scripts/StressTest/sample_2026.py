years_back_premise = 5
years_back_hypothesis = 6

# the hypothesis refers to the same comparison between John's and Tom's age as the premise, but with a different time frame
if years_back_hypothesis!= years_back_premise:
    # check if the time frame in the hypothesis contradicts the time frame in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are identical in terms of the comparison they make, but with different time frames
    # hence, the hypothesis cannot be explicitly entailed from the premise, but also does not contradict it
    label = "neutral"

print(label)
