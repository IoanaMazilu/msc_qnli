gdp_growth_1990s = 0.045

# the hypothesis mentions the GDP growth in the 1990s, which is also mentioned in the premise
if gdp_growth_1990s!= 0.045:
    # check if the gdp growth in the hypothesis contradicts the gdp growth reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
