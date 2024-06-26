# define variables for the premise and hypothesis
premise = "Experts determined that the two explosive devices were planted in one of the trees in the area,'' the ministry said, adding that an investigation was under way."
hypothesis = "It says that two explosive devices were in trees in the area."

# extract the relevant information from the premise and hypothesis
premise_devices = premise.split("two explosive devices")[0].strip()
hypothesis_devices = hypothesis.split("two explosive devices")[0].strip()

# compare the information extracted from the premise and hypothesis
if premise_devices!= hypothesis_devices:
    # check if the information in the hypothesis contradicts the information in the premise
    label = "contradiction"
else:
    # if the information in the hypothesis does not contradict the information in the premise, we can infer entailment
    label = "entailment"

print(label)
