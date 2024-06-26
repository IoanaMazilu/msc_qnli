premise_members = 760
premise_lists = 10
premise_threshold = 1/4

hypothesis_members = 760
hypothesis_lists = 10
hypothesis_threshold = 4/4

# the hypothesis refers to a lower threshold than the premise
if hypothesis_threshold < premise_threshold:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a lower threshold, but the hypothesis value is consistent with the premise
    label = "neutral"

print(label)
