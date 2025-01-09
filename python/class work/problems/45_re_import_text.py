import re

# ### 1. Extract Email Addresses
# *Sample Text:*
# *Question:* Write a regex pattern to extract all unique email addresses from the text.
# ---
Sample_Text = "You can reach out to john.doe@example.com or jane.smith123@work-mail.org. Don't contact john.doe@example.com again."
pattern = re.compile(r"[a-zA-Z0-9]+\.[a-zA-Z0-9]+@[a-z-]+\.[a-z]+") 
email = pattern.findall(Sample_Text)
print(email)
print()

# ### 2. Extract Dates in Multiple Formats
# *Sample Text:*
# *Question:* Write a regex pattern to extract dates in YYYY-MM-DD, DD/MM/YYYY, and DD-MM-YYYY formats.
# ---
Sample_Text = "The project started on 2023-03-15 and will end by 15/07/2024. Another important date is 12-12-2023."
pattern = re.compile(r"\d{4}[/-]\d{2}[/-]\d{2}|\d{2}[/-]\d{2}[/-]\d{4}")
# pattern = re.compile(r"[0-9]+[/-][0-9]+[/-][0-9]+")
date = pattern.findall(Sample_Text)
print(date)
print()

# ### 3. Extract URLs
# *Sample Text:*
# *Question:* Write a regex pattern to extract all URLs from the text.
# ---
Sample_Text = "Visit our website at https://www.example.com for more details. You can also check our blog at http://blog.example.org."
pattern =  re.compile(r"https?://[a-z]+.[a-z]+.[a-z]+")
link = pattern.findall(Sample_Text)
print(link)
print()

# ### 4. Extract Phone Numbers
# *Sample Text:*
# *Question:* Write a regex pattern to extract phone numbers in formats like (123) 456-7890, +1-123-456-7890, and 123-456-7890.
# ---
Sample_Text = "For support, call us at (123) 456-7890 or +1-123-456-7890. You can also reach out to 123-456-7890."
# pattern=re.compile(r"\(\d{3}\) \d{3}-\d{4}|\d{3}-\d{3}-\d{4}|\d{1,3}-\d{1,3}-\d{1,3}")
pattern=re.compile(r"\+?1?-?\(?\d{3}\)? ?-?\d{3}-\d{4}")
phone = pattern.findall(Sample_Text)
print(phone)
print()

# ### 5. Extract Hashtags
# *Sample Text:*
# *Question:* Write a regex pattern to extract all hashtags from the text.
# ---
Sample_Text = "I thought to do this series of posting some beautiful scenes from cinema which tried to teach us something. Hope you will like it #manjummelboys #manjumalboys #kanmani #manjummel #kuttan #facts #trendingnow #viralvideos #trendingreels #fact #quotes #timeheals #timehealsallwounds #timehealseverything"
pattern = re.compile(r"\#[a-zA-z]+")
hashtags = pattern.findall(Sample_Text)
print(hashtags)
print()

# ### 6. Extract Monetary Amounts
# *Sample Text:*
# *Question:* Write a regex pattern to extract monetary amounts in formats like $1,234.56 and €50.00.
# ---
Sample_Text = "The total cost is $1,234.56, and the discount is €50.00. Your final amount to pay is $1,184.56."
pattern=re.compile(r"[€$][0-9.,]+\d{2}")
amount = pattern.findall(Sample_Text)
print(amount)
print()

# ### 7. Extract words ending with "ing"
Sample_Text = "I am running and singing while thinking about something interesting being discussed."
pattern = re.compile(r"[a-zA-Z]+ing")
words = pattern.findall(Sample_Text)
print(words)
print()

# ### 8. Write a regular expression to extract all sentences from a paragraph that end with a question mark.
# Example:
Sample_Text = "How are you? I hope you're doing well. What is going on?"
pattern = re.compile(r"[A-Z][a-z ]+\?")
sentences = pattern.findall(Sample_Text)
print(sentences)