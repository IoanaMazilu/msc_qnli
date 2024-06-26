apples_premise = 360
apples_hypothesis = 460

# The hypothesis states a number of apples that Anita could have, which is mentioned in the premise
if apples_premise >= apples_hypothesis:
    # check if the number of apples in the premise contradicts the hypothesis that Anita has less than 'apples_hypothesis'
    label = "contradiction"
elif apples_premise == apples_hypothesis - 1:
    # if Anita has exactly one apple less than 'apples_hypothesis', the premise can entail the hypothesis
    label = "entailment"
else:
    # any number of apples less than 'apples_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
