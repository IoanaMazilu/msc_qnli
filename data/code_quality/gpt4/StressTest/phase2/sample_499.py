shirt_premise = 6
shirt_hypothesis = 1

# the hypothesis talks about the number of shirts in an outfit, referenced also in the premise
if shirt_hypothesis >= shirt_premise:
    # check if the hypothesis value contradicts the estimate of less than 'shirt_premise'
    label = "contradiction"
elif shirt_hypothesis < shirt_premise:
    # any number of shirts less than 'shirt_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
