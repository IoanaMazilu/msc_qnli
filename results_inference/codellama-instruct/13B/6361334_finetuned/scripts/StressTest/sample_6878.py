amar_age = 20
akbar_age = 25
anthony_age = 21
total_ages_premise = 66
total_ages_hypothesis = 66

# the hypothesis refers to the total age of Amar, Akbar and Anthony mentioned in the premise
if total_ages_hypothesis >= total_ages_premise:
    # check if the estimate of 'total_ages_hypothesis' contradicts the total age of Amar, Akbar and Anthony in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
