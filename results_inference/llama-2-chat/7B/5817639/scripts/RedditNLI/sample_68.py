premise = "Jobs Report: U.S. Economy Added 321,000 Jobs In November, Unemployment Steady At 5.8%"
hypothesis = "U.S. Economy Added 321,000 Jobs in November; Unemployment Rate Is 5.8%"

# define variables for the numerical entities in the premise and hypothesis
premise_jobs = 321000
premise_unemployment = 5.8

# extract the quantities from the premise and hypothesis
hypothesis_jobs = float(hypothesis.split(";")[1].strip())
hypothesis_unemployment = float(hypothesis.split(";")[2].strip())

# compare the quantities
if premise_jobs!= hypothesis_jobs:
    # check if the number of jobs in the hypothesis contradicts the number of jobs in the premise
    label = "contradiction"
elif premise_unemployment!= hypothesis_unemployment:
    # check if the unemployment rate in the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the premise and hypothesis have the same number of jobs and unemployment rate, we can infer entailment
    label = "entailment"

print(label)
