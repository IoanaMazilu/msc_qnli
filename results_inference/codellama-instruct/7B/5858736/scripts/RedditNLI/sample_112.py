# extract the numerical information from the premise and hypothesis
premise_filings = 14
hypothesis_filings = 14

# check if the number of filings in the hypothesis contradicts the number of filings in the premise
if hypothesis_filings!= premise_filings:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
