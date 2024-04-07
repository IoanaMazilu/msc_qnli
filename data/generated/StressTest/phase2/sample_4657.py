# Premise: The X & co having such a sales structure out of their whole sales more than 40% of the customers are corporate companies out of these 20% of them are related to banking sector and 60% of the corporate companies related to banking sector having their head quarters in USA.
# Hypothesis: The X & co having such a sales structure out of their whole sales 70% of the customers are corporate companies out of these 20% of them are related to banking sector and 60% of the corporate companies related to banking sector having their head quarters in USA.
# Golden Label: neutral

corporate_customers_premise = 40
corporate_customers_hypothesis = 70
banking_sector_customers_premise = 20
banking_sector_customers_hypothesis = 20
usa_headquarters_customers_premise = 60
usa_headquarters_customers_hypothesis = 60

# hypothesis refers to the percentage of corporate customers, banking sector customers and customers with head quarters in USA mentioned in the premise
if corporate_customers_hypothesis < corporate_customers_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif banking_sector_customers_hypothesis != banking_sector_customers_premise or usa_headquarters_customers_hypothesis != usa_headquarters_customers_premise:
    # check if the percentage of banking sector customers or customers with head quarters in USA in hypothesis contradicts with the premise
    label = "contradiction"
elif corporate_customers_hypothesis > corporate_customers_premise:
    # if the percentage of corporate customers in hypothesis is more than premise, we can not fully and explicitly entail the hypothesis from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

