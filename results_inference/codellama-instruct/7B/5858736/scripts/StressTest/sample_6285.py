# the hypothesis refers to a lower score on a test, which may or may not contradict the premise
if robin_score_premise <= 70:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a higher score on a test, which cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)
