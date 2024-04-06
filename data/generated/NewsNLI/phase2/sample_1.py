# Premise: Sharper, 38, faces rape charges in Arizona and California and a warrant for his arrest was issued in Louisiana.
# Hypothesis: Darren Sharper has been charged in two states while another seeks his arrest.
# Golden Label: entailment

charges_premise = 2
arrest_warrant_premise = 1
charges_hypothesis = 2
arrest_warrant_hypothesis = 1

# the hypothesis mentions the number of states where charges have been issued and the number of states seeking an arrest warrant, which are also mentioned in the premise
if charges_hypothesis != charges_premise:
    # check if the number of charges in the hypothesis contradicts the number of charges reported in the premise
    label = "contradiction"
elif arrest_warrant_hypothesis != arrest_warrant_premise:
    # check if the number of arrest warrants from the hypothesis contradicts the number of arrest warrants in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

