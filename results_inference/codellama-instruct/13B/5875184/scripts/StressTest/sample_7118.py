premise_germs = 4.32 * 10 ** 6
hypothesis_germs = 4.32 * 10 ** 6
premise_dishes = 10800
hypothesis_dishes = 10800

# the hypothesis refers to the number of germs in the lab, which is mentioned in the premise
if premise_germs <= hypothesis_germs:
    # check if the estimate of 'hypothesis_germs' contradicts the number of germs in the premise
    label = "contradiction"
elif premise_dishes!= hypothesis_dishes:
    # check if the number of dishes in the hypothesis contradicts the number of dishes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
