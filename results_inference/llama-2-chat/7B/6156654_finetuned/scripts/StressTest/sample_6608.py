years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis talks about the years and interest rate, which are also mentioned in the premise
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate!= 4:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)