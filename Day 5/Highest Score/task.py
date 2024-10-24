student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)

print(total_score)

sum=0
for score in student_scores:
    sum +=score
print(sum)
print(range(1, 10))



# Max and min  WITH USING max() and min()
max=max(student_scores)
min=min(student_scores)
print(f" min number in a list is {min}")
print(f" max number in a list is {max}")



# Max and min  WITHOUT USING max() and min()
scores=[8 ,65 ,89 ,86 ,55 ,91 ,64 ,8,9]
max_score=0;
for score in scores:
    if score>max_score:
        max_score=score
    min_score=max_score
    if score<min_score:
        min_score=score
print(f" min number in a list is {min_score}")
print(f" max number in a list is {max_score}")
