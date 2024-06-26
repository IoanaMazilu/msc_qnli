year_premise = 2006
year_hypothesis = 2008

# the hypothesis and premise mention the year the rate was raised after the Fed
if year_premise!= year_hypothesis:
    # check if the year in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # the premise and hypothesis are about different countries raising their rates for the first time after the Fed
    # the hypothesis cannot be explicitly entailed from the premise, but it does not contradict it either
    label = "neutral"

print(label)
