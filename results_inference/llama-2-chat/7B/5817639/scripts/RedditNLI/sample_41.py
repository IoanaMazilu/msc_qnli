# Premise: Norway's Current Account Surplus Adds US$4.61 Billion In Quarter 2 Of 2017 To The Economy.
premise_quarter = 2
premise_year = 2017

# Hypothesis: South Korea's Current Account Surplus Added USD 7.01 Billion In June Of 2017 To The Economy.
hypothesis_quarter = 2
hypothesis_year = 2017

# compare the quarter and year of the premise and hypothesis
if premise_quarter!= hypothesis_quarter or premise_year!= hypothesis_year:
    # check if the quarter and year of the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the premise and hypothesis have the same quarter and year, check if the amount added to the economy is different
    if abs(premise_quarter - hypothesis_quarter) > 1 or abs(premise_year - hypothesis_year) > 1:
        label = "contradiction"
    else:
        # the premise and hypothesis have the same quarter and year, and the amount added to the economy is the same
        label = "entailment"

print(label)
