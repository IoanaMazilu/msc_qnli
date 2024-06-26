years_premise = 5
years_hypothesis = 8

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_premise > years_hypothesis:
    # check if the time frame in the premise contradicts the time frame in the hypothesis
    label = "contradiction"
elif years_premise < years_hypothesis:
    # check if the time frame in the premise can be fully and explicitly entailed from the time frame in the hypothesis
    label = "entailment"
else:
    # if the time frames are equal, we can infer neutrality
    label = "neutral"

print(label)
