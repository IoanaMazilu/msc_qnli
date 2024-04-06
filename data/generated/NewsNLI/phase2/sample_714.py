# Premise: '' An Unexpected Journey'' was followed closely by'' Django Unchained,'' which has an estimated download count of 8.1 million -- just 300,000 fewer than'' The Hobbit,'' even though'' The Hobbit's'' worldwide box office take was more than twice what Django made.
# Hypothesis: '' The Hobbit:An Unexpected Journey'' had about 8.4 million downloads.
# Golden Label: neutral

download_count_django = 8.1
download_count_hobbit = download_count_django + 0.3

# The hypothesis mentions the download count of ''The Hobbit: An Unexpected Journey'', which can be calculated from the premise 
if download_count_hobbit != 8.4:
    # check if the download count in the hypothesis contradicts the download count calculated from the premise
    label = "contradiction"
else:
    # if the download count in the hypothesis does not contradict the download count from the premise, we can infer entailment
    label = "entailment"

print(label)

