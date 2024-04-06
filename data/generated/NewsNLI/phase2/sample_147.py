# Premise: The EU force confirmed that six pirates have boarded the 180-meter long bulk carrier, with two attack skiffs in tow.
# Hypothesis: European Union Naval Force say six pirates boarded 180-meter long carrier.
# Golden Label: entailment

pirates_premise = 6
pirates_hypothesis = 6
carrier_length_premise = 180
carrier_length_hypothesis = 180

# the hypothesis mentions the number of pirates and the length of the carrier, which are also mentioned in the premise
# however, the hypothesis does not mention the two attack skiffs mentioned in the premise
if pirates_hypothesis != pirates_premise:
    # check if the number of pirates in the hypothesis contradicts the number of pirates reported in the premise
    label = "contradiction"
elif carrier_length_hypothesis != carrier_length_premise:
    # check if the length of the carrier from the hypothesis contradicts the length of the carrier in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality as there is missing information
    label = "neutral"

print(label)

