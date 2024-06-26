apples_billy_premise = 5
apples_billy_hypothesis = 4

# the hypothesis talks about the number of apples Billy has, referenced also in the premise
if apples_billy_premise <= apples_billy_hypothesis:
    # check if the hypothesis value contradicts the exact number of apples 'apples_billy_premise'
    label = "contradiction"
else:
    # the exact number of apples Billy has is mentioned in the premise, 
    # therefore the hypothesis can be explicitly entailed from the premise
    label = "entailment"

print(label)
