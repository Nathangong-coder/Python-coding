from cgi import print_arguments


msg1='''(y=3x'''
msg2='''+7)'''
print(msg1+msg2)

msg3='''(y=3x+7)'''
print(msg3)

print('(y=3x+7)')

print("(y=3x+7)")

print('''(y=3x+7)''')

x="3x+4"
msg='''y='''

print(msg+x)

x=1
y=(3*x+7)
print(y)

#my bug

x=;1
y=(e*x+3*7)
print(x,y)