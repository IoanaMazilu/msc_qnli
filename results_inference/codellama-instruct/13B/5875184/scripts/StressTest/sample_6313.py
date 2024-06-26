premise_males = 2
premise_females = 3
hypothesis_males = 4
hypothesis_females = 3

# the hypothesis refers to the number of males and females mentioned in the premise
if hypothesis_males <= premise_males and hypothesis_females <= premise_females:
    # check if the estimate of 'hypothesis_males' and 'hypothesis_females' contradicts the number of males and females in the premise
    label = "contradiction"
elif hypothesis_males == premise_males and hypothesis_females == premise_females:
    # check if the number of males and females in the hypothesis is consistent with the number of males and females in the premise
    label = "neutral"
else:
    # the premise gives only an estimate for the number of males and females
    # any number of males and females greater than 'premise_males' and 'premise_females' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
