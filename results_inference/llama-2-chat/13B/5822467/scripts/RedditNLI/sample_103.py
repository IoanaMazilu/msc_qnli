premise_rate = "2008"
hypothesis_rate = "2006"

# extract the year values as integers
premise_year = int(premise_rate)
hypothesis_year = int(hypothesis_rate)

# compare the years
if premise_year!= hypothesis_year:
    # the years in the premise and hypothesis do not match, so there is a contradiction
    label = "contradiction"
elif premise_year < hypothesis_year:
    # the premise mentions a year earlier than the hypothesis, so there is a contradiction
    label = "contradiction"
else:
    # the premise and hypothesis mention the same year, so there is no contradiction
    label = "neutral"

print(label)
