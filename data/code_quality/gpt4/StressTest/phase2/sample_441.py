efficiency_premise = 20
efficiency_hypothesis = 10

# the hypothesis talks about the efficiency difference between Tanya and Sakshi, referenced also in the premise
if efficiency_premise <= efficiency_hypothesis:
    # check if the efficiency difference in the premise contradicts the hypothesis 
    label = "contradiction"
elif efficiency_hypothesis < efficiency_premise:
    # the hypothesis makes a lower bound claim about the efficiency difference which is entailed by the premise
    label = "entailment"
else:
    # if the efficiency difference in the hypothesis does not contradict or can be entailed from the premise, we infer neutrality
    label = "neutral"

print(label)
