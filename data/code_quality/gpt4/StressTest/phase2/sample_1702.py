hunters_premise = 4500
hunters_hypothesis = 1500

# the hypothesis talks about the number of hunters in Piscataquis County, referenced also in the premise
if hunters_hypothesis >= hunters_premise:
    # check if the number of hunters in the hypothesis contradicts the estimate of less than 'hunters_premise'
    label = "contradiction"
elif hunters_hypothesis < hunters_premise:
    # the premise gives only an estimate for the number of hunters
    # any number of hunters less than 'hunters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
