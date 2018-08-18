print('Hello, Django girls!')

print("--Awesome or Not--")

person = "Romy"
pad = " "
operator = "is"
disagree = "is not"
state = "great"
print(person + pad + operator + pad + state)

if state == "awesome":
    print('Life' + pad + operator + pad + 'awesome!!')
elif state != "great":
    print('Life' + pad + operator + pad + 'great!!')
else:
    print('It' + pad + disagree + pad + 'awesome!!')

print("--Hi--")

def hi(name):
    if name == 'Ola':
        print('The name is Ola!')
    elif name == 'Sonja':
        print('The name is Sonja!')
    else:
        print('The name is anonymous!')

hi("Ola")

print("--Names--")

def hello():

    girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', person]
    for names in girls:
        print('Hi ' + names + '!')
        print('Next girl')

hello()

print("--FuncTest--")

def greet(FuncTest):
    print('Greetings ' + girlname + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', person]
for girlname in girls:
    greet(girlname)
    print('Next girl')

print("--Range--")

for i in range(1, 6):
    print(i)