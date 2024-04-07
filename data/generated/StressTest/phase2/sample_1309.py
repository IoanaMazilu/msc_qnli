# Premise: If there are less than 20 Pens, the number of Markers in Jenna's desk is :
# Hypothesis: If there are 10 Pens, the number of Markers in Jenna's desk is :
# Golden Label: neutral

pens_premise = 20
pens_hypothesis = 10

# the hypothesis talks about the number of pens referenced in the premise
if pens_hypothesis >= pens_premise:
    # check if the number of pens in the hypothesis contradicts the estimate of less than 'pens_premise'
    label = "contradiction"
else:
    # the premise doesn't provide any numerical information about the number of markers, so no value would contradict it
    # but the hypothesis can't be explicitly entailed from the premise either
    label = "neutral"

print(label)

