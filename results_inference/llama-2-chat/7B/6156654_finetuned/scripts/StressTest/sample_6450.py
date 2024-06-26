# The hypothesis refers to the number of passengers from North America, which is also mentioned in the premise
if premise.get("entailment", False):
    # If the number of passengers from North America in the premise is less than 5/12,
    # it is also less than 5/12 in the hypothesis
    if premise.get("from_north_america", 0) < 5/12:
        # check if the number of passengers from North America in the hypothesis contradicts the premise
        label = "contradiction"
    else:
        # if the number of passengers from North America in the hypothesis is less than 5/12,
        # it is consistent with the premise, but cannot be explicitly entailed from the premise
        label = "neutral"
else:
    # If the premise does not mention the number of passengers from North America,
    # it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
