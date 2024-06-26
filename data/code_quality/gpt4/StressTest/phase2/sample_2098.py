year_premise = 3979
year_hypothesis = 1979
percentage_passengers_premise = 1/3
percentage_passengers_hypothesis = 1/3
total_passengers_premise = 37.3 * 10**6
total_passengers_hypothesis = 37.3 * 10**6

# the hypothesis refers to the percentage of airline passengers and the year mentioned in the premise
if year_hypothesis >= year_premise:
    # check if the hypothesis year contradicts the estimate of less than 'year_premise'
    label = "contradiction"
elif percentage_passengers_premise != percentage_passengers_hypothesis or total_passengers_premise != total_passengers_hypothesis:
    # check if the percentage of passengers or total passengers contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
