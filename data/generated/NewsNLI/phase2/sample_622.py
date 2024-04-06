# Premise: The appraisal Joe had done on the black diamond put its value at approximately $14.5 million, according to Hughes, who said he saw the certificate of authenticity.
# Hypothesis: Black diamond in the home button was appraised at $14.5 million.
# Golden Label: neutral

black_diamond_value_premise = 14.5e6
black_diamond_value_hypothesis = 14.5e6

# the hypothesis mentions the value of the black diamond, which is also referenced in the premise
if black_diamond_value_hypothesis != black_diamond_value_premise:
    # check if the black diamond value in the hypothesis contradicts the black diamond value reported in the premise
    label = "contradiction"
else:
    # if the black diamond value in the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

