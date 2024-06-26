lawn_rake_premise_john = 60
lawn_rake_premise_todd = 60
lawn_rake_hypothesis_john = 30
lawn_rake_hypothesis_todd = 60

# the hypothesis values are compared to the premise values
if lawn_rake_hypothesis_john <= lawn_rake_premise_john:
    # check if the hypothesis value contradicts the estimate of less than 'lawn_rake_premise_john'
    label = "contradiction"
elif lawn_rake_hypothesis_todd!= lawn_rake_premise_todd:
    # check if the hypothesis value contradicts the estimate of 'lawn_rake_premise_todd'
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
