# 1.Given two sets of numbers, determine if one set is a subset or superset of the other. Then, find the difference between the two sets.
set_X = {1, 2, 3, 4, 5}
set_Y = {3, 4, 5}
if set_X.issubset(set_Y):
    print("Set X is a subset of Set Y")
    diff = set_X.difference(set_Y)
    print("Difference:", diff)
elif set_X.issuperset(set_Y):
    print("Set X is a superset of Set Y")
    diff = set_X.difference(set_Y)
    print("Difference:", diff)
else:
    print("Set X is neither subset nor superset of Set Y")


# 2.You have a list of all possible elements (e.g., numbers from 1 to 10), and a set of observed elements. Determine which elements are missing.
all_elements = set(range(1, 11))
observed_elements = {2, 4, 6, 8, 10}
missing_elements = all_elements.difference(observed_elements) 
print("Missing elements:", missing_elements)


# 3.You are given a list of email addresses. Write a function to detect if there are any duplicates.
email_list = ['alice@example.com', 'bob@example.com', 'charlie@example.com', 'alice@example.com']
email_set = set(email_list)

if len(email_set) == len(email_list):
    print("No duplicates found")
else:
    print("Duplicates found")


# 4.You have two sets representing the skills of two different employees. Determine the common skills between them, and also identify unique skills that each employee has.
employee_A = ('Python', 'Java', 'SQL', 'AWS') 
employee_B = ('Python', 'JavaScript', 'SQL', 'Docker')
common_skills = set(employee_A).intersection(set(employee_B))
print("Common Skills: ",common_skills)

employee_A_unique = set(employee_A).difference(set(employee_B))
print("Employee A Unique skills: ",employee_A_unique)
employee_B_unique = set(employee_B).difference(set(employee_A))
print("Employee B Unique skills: ",employee_B_unique)


# 5.You manage a team where members have different language proficiencies. Given three sets of languages known by different team members, determine:
# 1. The languages known by everyone.
# 2. The languages known by at least one team member.
member_1 = {'English', 'Spanish', 'German'}
member_2 = {'English', 'French', 'German'}
member_3 = {'English', 'Spanish', 'Mandarin'}

common_languages = member_1.intersection(member_2.intersection(member_3))
print("Common languages: ", common_languages)

all_languages = member_1.union(member_2.union(member_3))
print("All languages: ", all_languages)