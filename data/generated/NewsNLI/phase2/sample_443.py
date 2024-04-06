# Premise: Pay $20 at the Istanbul airport visa booth before going to immigration.
# Hypothesis: In Turkey, pay $20 at the Istanbul airport visa booth.
# Golden Label: entailment

visa_fee_premise = 20
visa_fee_hypothesis = 20

# the hypothesis mentions the visa fee at the Istanbul airport, which is also referenced in the premise
if visa_fee_hypothesis != visa_fee_premise:
    # check if the visa fee in the hypothesis contradicts the visa fee in the premise
    label = "contradiction"
else:
    # if the visa fee in the hypothesis does not contradict the visa fee in the premise, we can infer entailment
    label = "entailment"

print(label)

