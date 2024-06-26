interest_years_premise = 7
interest_years_hypothesis = 2
interest_received_premise = 400
interest_received_hypothesis = 400

# the hypothesis refers to the years of investment and interest received, both mentioned in the premise
if interest_years_hypothesis >= interest_years_premise:
    # check if the years of investment in the hypothesis contradicts the estimate of less than 'interest_years_premise' 
    label = "contradiction"
elif interest_received_hypothesis != interest_received_premise:
    # check if the interest received in the hypothesis contradicts the interest received in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
