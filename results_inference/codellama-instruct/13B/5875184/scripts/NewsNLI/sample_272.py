premise = "The lawyer for Fattal and Bauer, Masoud Shafiee, told CNN the $1 million bail had been paid by the Omani government."
hypothesis = "The $1 million bail is paid by the Omani government, their attorney says."

# extract the numerical entities from the premise and hypothesis
premise_bail = 1000000
hypothesis_bail = 1000000

# compare the bail amounts
if premise_bail!= hypothesis_bail:
    # check if the bail amount in the hypothesis contradicts the bail amount reported in the premise
    label = "contradiction"
else:
    # if the bail amount in the hypothesis is the same as the bail amount reported in the premise, we can infer entailment
    label = "entailment"

print(label)
