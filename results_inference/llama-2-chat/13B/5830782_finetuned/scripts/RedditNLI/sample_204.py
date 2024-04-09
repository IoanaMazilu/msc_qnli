jobs_premise = 5000
percentage_workforce_hypothesis = 5

# the hypothesis and premise mention the number of jobs Intel plans to cut and the percentage of the workforce
# but they do not mention the same year, so we cannot infer from the hypothesis the exact number of jobs in the premise
if jobs_premise!= None and jobs_premise >= percentage_workforce_hypothesis/100 * Intel.workforce_size:
    # check if the number of jobs in the premise is greater than or equal to the percentage of the workforce in the hypothesis
    # this would mean that the hypothesis is entailed by the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but we cannot infer the exact number of jobs from the hypothesis
    label = "neutral"

print(label)
