premise_city_a = "A"
premise_city_b = "B"
premise_andrew_driven_less_than_5_hr_at_40_mph = 5
premise_andrew_driven_3_hr_at_60_mph = 3

hypothesis_city_a = "A"
hypothesis_city_b = "B"
hypothesis_andrew_driven_1_hr_at_40_mph = 1
hypothesis_andrew_driven_3_hr_at_60_mph = 3

# the hypothesis talks about the number of hours and speed at which Andrew drove
if hypothesis_andrew_driven_1_hr_at_40_mph <= premise_andrew_driven_less_than_5_hr_at_40_mph:
    # check if the hypothesis value contradicts the estimate of less than 'premise_andrew_driven_less_than_5_hr_at_40_mph'
    label = "contradiction"
elif hypothesis_andrew_driven_3_hr_at_60_mph <= premise_andrew_driven_3_hr_at_60_mph:
    # check if the hypothesis value contradicts the estimate of 'premise_andrew_driven_3_hr_at_60_mph'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
