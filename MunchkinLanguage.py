import time

print("You are using Munchkin version 0.0.0.0, a programming language made with Python.")
print("For credits, run \"credits\".")
print("For help, run \"help\".")
print("To learn more about Munchkin, go to https://github.com/Munchkin-Language")
shell = 'true'
while shell == 'true':
    shell = 'true'
    s = input('>>> ')
    if s.startswith('out') and s[3] == '(' and ')' in s:
        to_print = s.split('(')[1].split(')')[0]
        if (to_print[0] == "'" and to_print[-1] == "'") or (to_print[0] == '"' and to_print[-1] == '"'):
            print(to_print[1:-1])
        def out(variable):
            return variable
    if s == "help":
        print("Here is a list of some basic commands:")
        print("out()")
        print("kill")
        print("credits")
    if s == "kill":
        exit()
    if s == "credits":
        print("Munchkin Credits:")
        print("Original code and ideas made by GitHub user JabbaTheMutt")
        print("Official Munchkin GitHub organization is https://github.com/Munchkin-Language")
        print("Code shortening, enhancing, and help by the Python Discord Server https://discord.gg/python")
        print("Munchkin official Discord server https://discord.gg/vFRJfnqWRz")
        print("The fantastic Python Discord Members that helped me:")
        print("Martysh12")
        print("u/Hacka4771")
        print("Assile")
        print("Thanks for using Munchkin!")