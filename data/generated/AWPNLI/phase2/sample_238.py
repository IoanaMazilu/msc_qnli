# Premise: You are reading a book with 120.0 pages, and you want to read the same number of pages each night.
# Hypothesis: You would have 12.0 pages to read each night to finish in 10.0 days.
# Golden Label: entailment

total_pages_premise = 120.0
pages_per_night_hypothesis = 12.0
total_days_hypothesis = 10.0

# the hypothesis refers to the number of pages to be read each night, and the total number of days to finish the book
# we can calculate the expected number of pages to read each night from the premise
expected_pages_per_night_premise = total_pages_premise / total_days_hypothesis
if pages_per_night_hypothesis != expected_pages_per_night_premise:
    # check if the number of pages to be read each night in the hypothesis contradicts the calculated number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment" 

print(label)

