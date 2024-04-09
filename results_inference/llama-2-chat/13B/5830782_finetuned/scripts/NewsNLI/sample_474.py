# the number of matches played by Varane is not mentioned in the hypothesis
matches_played_premise = 23

# the hypothesis mentions the relegation of Lens and Varane's displays, which are also mentioned in the premise
# however, the hypothesis does not mention the number of matches played by Varane
if matches_played_premise in [23]:
    # check if the number of matches played by Varane is mentioned in the hypothesis
    label = "neutral"
else:
    # if the number of matches played by Varane is not mentioned in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
