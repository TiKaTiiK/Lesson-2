# 1. ვიქტორინა
# შეადგინე ვიქტორინის პროგრამა. მომხმარებელს უნდა დავუსვათ კითხვა: “რომელი
# იმპერიის მიერ აგებული წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქციონირებს
# დღესაც?”
# სავარაუდო პასუხები:
# 1. შუმერთა
# 2. სელჩუკთა
# 3. რომის
# 4. მონღოლთა
# მომხმარებელმა უნდა შეიყვანოს სწორი პასუხის ნომერი ან თავად სწორი პასუხი.
# შეცდომის შემთხვევაში იბეჭდება:
# „არა! სწორი პასუხია რომის!“
# სწორი პასუხის შემთხვევაში იბეჭდება:
# „სწორია!“

# print("By which empire's built water supply system (aqveduct) is still functioning today? ")
#
# num1 = "1"
# num2 = "2"
# num3 = "3"
# num4 = "4"
# dot = "."
# name1 = "Sumerians"
# name2 = "Seljuks"
# name3 = "Rome"
# name4 = "Mongols"
#
# answer = input(f"""
# {num1}{dot} {name1}
# {num2}{dot} {name2}
# {num3}{dot} {name3}
# {num4}{dot} {name4}
#
# """)
#
# if answer == f"{num3}":
#     print("Correct!")
# elif answer == f"{name3}":
#     print("Correct!")
# else:
#     print(f"No! Correct Answer is {name3}!")

# 2. გამრავლების ტაბულა
# ორმაგი for ციკლის_ის დახმარებით დაბეჭდე გამრავლების ტაბულა 1_დან
# მომხმარებლის მიერ შეყვანილი მთელი რიცხვის ჩათვლით.

# def multiplication_table(num):
#
#   for i in range(1, num + 1):
#     for j in range(1, num + 1):
#       print(f"{i * j:4}", end=" ")
#     print()
#
# number = int(input("Enter a number to generate the multiplication table: "))
#
# multiplication_table(number)

# 3. თუთიყუშის პროგრამა
# დაწერე პროგრამა _ თუთიყუში. პროგრამამ უნდა გაიმეოროს რასაც ეტყვი მანამ სანამ არ
# შეიყვან სიტყვას quit, თუმცა წინ დაურთოს კითხვა „User Said Whaaat?!”
# თუ შევიყვანეთ სიტყვა Hello დაიბეჭდება
# „User Said Whaaat?!”
# “User Said Hello”

# while True:
#
#   user_input = input("User Said Whaaat?! ").lower()
#
#   if user_input == "quit":
#
#     break
#
#   if user_input == "hello":
#     print("The customer said what?!")
#     print("The user said hello")
#
# print("Okay, exiting the program.")
