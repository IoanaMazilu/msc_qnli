total_ages_premise = 66
total_ages_hypothesis = 86

# the hypothesis refers to the total ages of Amar, Akbar and Anthony mentioned in the premise
if total_ages_hypothesis <= total_ages_premise:
    # check if the 'total_ages_hypothesis' contradicts the total ages from the premise
    label = "contradiction"
elif total_ages_hypothesis > total_ages_premise:
    # if 'total_ages_hypothesis' is greater than 'total_ages_premise', it does not contradict it but entailment is not explicit
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
