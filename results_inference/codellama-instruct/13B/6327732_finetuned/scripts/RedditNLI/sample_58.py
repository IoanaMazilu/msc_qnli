premise = "U.S. Payrolls Rebound to 164,000 Gain; Jobless Rate Hits 3.9%."
hypothesis = "BloombergMarkets U.S. Payrolls Rise 164,000 While Jobless Rate Falls to 3.9%."

# extract the numerical entities from the premise and hypothesis
premise_payrolls = 164000
premise_jobless_rate = 3.9
hypothesis_payrolls = 164000
hypothesis_jobless_rate = 3.9

# compare the numerical entities in the premise and hypothesis
if premise_payrolls!= hypothesis_payrolls:
    # check if the number of payrolls in the hypothesis contradicts the number of payrolls in the premise
    label = "contradiction"
elif premise_jobless_rate!= hypothesis_jobless_rate:
    # check if the jobless rate in the hypothesis contradicts the jobless rate in the premise
    label = "contradiction"
else:
    # if the numerical entities in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
