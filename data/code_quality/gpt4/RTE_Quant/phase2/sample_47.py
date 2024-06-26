population_support_premise = 50
population_support_hypothesis = 50

# the hypothesis talks about the percentage of people supporting independence in Wales, same as in the premise
# however, the premise mentions that it is doubtful if even half the population would support it
# while the hypothesis predicts that probably less than 50% would support it

if population_support_hypothesis <= population_support_premise:
    # if the predicted support from the hypothesis is less than or equal to the doubtfully estimated support from the premise, we can infer entailment
    label = "entailment"
else:
    # if the predicted support from the hypothesis is more than the doubtfully estimated support from the premise, we infer contradiction
    label = "contradiction"

print(label)
