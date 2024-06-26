tariff_premise = 25
tariff_hypothesis = 25
value_premise = 200
value_hypothesis = 200

# the hypothesis and premise mention the same tariff percentage on the same value of goods
if tariff_hypothesis != tariff_premise:
    # check if the tariff percentage in the hypothesis contradicts the tariff percentage in the premise
    label = "contradiction"
elif value_hypothesis != value_premise:
    # check if the value of goods in the hypothesis contradicts the value of goods in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
