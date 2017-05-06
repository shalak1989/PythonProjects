# emails = ['me@gmail.com', 'you@hotmail.com', 'she@hotmail.com']
#
# for item in emails:
#     if 'gmail' in item:
#         print(item)
#
# def currency_converter(rate, euros):
#     dollars = euros*rate
#     return dollars
# r = input('Enter Rate: ')
# e = input('Enter euros: ')
# # currency_converter(float(r), float(e))
#
# password = ''
# while password != 'python123':
#     password=input('Enter password: ')
#     if password == 'python123':
#         print("You are logged in!")
#     else:
#         print("Sorry try again!")

names = ['james', 'john', 'jack']
email_domains = ['gmail', 'hotmail', 'yahoo']

for i,j in zip(names, email_domains):
    print(i, j)
