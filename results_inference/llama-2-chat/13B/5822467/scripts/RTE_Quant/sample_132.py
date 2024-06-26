premise_carl_lewis_records = "more than a decade ago"
hypothesis_carl_lewis_medals = "eighteen gold medals"
hypothesis_carl_lewis_records = "21 world records"

# define variables with representative names for the numerical entities in both inputs
carl_lewis_records_premise = premise_carl_lewis_records.split(" ")[1]
carl_lewis_records_hypothesis = hypothesis_carl_lewis_records.split(" ")[1]

# extract all quantities as valid numbers (integers or floats)
carl_lewis_records_premise = int(carl_lewis_records_premise)
carl_lewis_records_hypothesis = int(carl_lewis_records_hypothesis)

# perform calculations if necessary
# no calculations are necessary in this case

# compare the variables to infer the label
if carl_lewis_records_hypothesis > carl_lewis_records_premise:
    # the hypothesis talks about a higher number of records than the premise, so we have entailment
    label = "entailment"
elif carl_lewis_records_hypothesis < carl_lewis_records_premise:
    # the hypothesis talks about a lower number of records than the premise, so we have contradiction
    label = "contradiction"
else:
    # the number of records in the hypothesis and premise are the same, so we have neutrality
    label = "neutral"

print(label)
