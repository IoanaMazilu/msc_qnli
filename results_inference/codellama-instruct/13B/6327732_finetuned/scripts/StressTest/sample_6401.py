# extract the numerical entities from the premise and hypothesis
premise_miami_airport = 1/2
premise_kennedy_airport = 1/2
premise_logan_airport = 4
hypothesis_miami_airport = 3/2
hypothesis_kennedy_airport = 3/2
hypothesis_logan_airport = 4

# compare the values of the variables to determine the relation between the premise and hypothesis
if premise_miami_airport!= hypothesis_miami_airport:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif premise_kennedy_airport!= hypothesis_kennedy_airport:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif premise_logan_airport!= hypothesis_logan_airport:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis is consistent with the premise
    label = "entailment"

print(label)
