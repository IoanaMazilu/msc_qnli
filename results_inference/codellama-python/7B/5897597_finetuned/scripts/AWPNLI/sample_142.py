pages_read_yesterday_premise = 21.0
pages_read_today_premise = 17.0
total_pages_hypothesis = 38.0

# the hypothesis refers to the total number of pages read, which are also mentioned in the premise
# compute the total number of pages read in the premise
total_pages_premise = pages_read_yesterday_premise + pages_read_today_premise
if total_pages_hypothesis!= total_pages_premise:
    # check if the total number of pages in the hypothesis contradicts the total number of pages from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
