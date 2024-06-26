# define variables for the premise and hypothesis
premise_passengers_miami = 1/2
premise_passengers_kennedy = 4*premise_passengers_miami
premise_passengers_logan = 4*premise_passengers_miami

hypothesis_passengers_miami = 3/2
hypothesis_passengers_kennedy = 4*hypothesis_passengers_miami
hypothesis_passengers_logan = 4*hypothesis_passengers_miami

# compute the number of passengers that used Logan Airport in the premise and hypothesis
premise_passengers_logan = premise_passengers_miami * 4
hypothesis_passengers_logan = hypothesis_passengers_miami * 4

# compare the number of passengers that used Logan Airport in the premise and hypothesis
if premise_passengers_logan!= hypothesis_passengers_logan:
    label = "contradiction"
else:
    label = "entailment"

print(label)
