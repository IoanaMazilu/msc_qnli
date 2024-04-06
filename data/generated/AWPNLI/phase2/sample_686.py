# Premise: Isabel had 2.0 pages of math homework and 4.0 pages of reading homework, and there are 5 total problems.
# Hypothesis: 1.2 problems were on each page on average.
# Golden Label: entailment

math_pages_premise = 2.0
reading_pages_premise = 4.0
total_problems_premise = 5
average_problems_per_page_hypothesis = 1.2

# the hypothesis refers to the average number of problems per page, which can be deduced from the premise
# compute the total number of pages from the premise
total_pages_premise = math_pages_premise + reading_pages_premise

# compute the average number of problems per page from the premise
average_problems_per_page_premise = total_problems_premise / total_pages_premise

if average_problems_per_page_hypothesis != average_problems_per_page_premise:
    # check if the average number of problems per page in the hypothesis contradicts the average number of problems per page from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

