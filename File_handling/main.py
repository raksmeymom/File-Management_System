# topic = "New"
topic = """ 
In this Course, we will learn about file handling in python
 """

# file = open("text.txt", "x")
# file.write(topic)
# file.close()

with open ("text.txt", "r") as read_file:
    print(read_file.read())