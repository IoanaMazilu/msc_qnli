invited_people_premise = 18.0
additional_people_premise = 12.0
tables_hypothesis = 10.0

# compute the total number of people held by the tables
total_people_tables = 3.0 * tables_hypothesis

# compare the number of tables in the hypothesis with the number of people held by the tables in the premise
if total_people_tables >= invited_people_premise:
    label = "entailment"
elif tables_hypothesis!= invited_people_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
