def check(li, showResult: bool = False):
    if len(li) > 5:
            return "Error: Too many problems."
    line1 = ""
    line2 = "" 
    line3 = ""
    line4 = ""
    
    for i, problem in enumerate(li):
        num1, operand, num2 = problem.split()
        
        if not operand in ["+","-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        
        #print(str(i) + "\t" + num1 + "\t" + num2)

        if len(num1) > 3:
            return "Error: Numbers cannot be more than four digits."
            quit()
            
        if  len(num2) > 3:
            return "Error: Numbers cannot be more than four digits."
            quit()
            
        
        if operand == '+':
            solution = int(num1) + int(num2)
        else:
            solution = int(num1) - int(num2)
        num_length = len(max([num1, num2], key=len))
        
        line1 += num1.rjust(num_length + 2)
        line2 += operand + num2.rjust(num_length + 1)
        line3 += "-" * (num_length + 2)
        line4 += str(solution).rjust(num_length + 2)

        if i < len(li)-1:
            line1 += " "
            line2 += " "
            line3 += " "
            line4 += " "

    vertical_format_output = line1 + "\n" + line2 + "\n" + line3    

    if showResult:
        vertical_format_output += "\n" + line4

    return vertical_format_output         
        
print(check(["3 + 855", "380 - 2", "45 + 43", "123 + 49"]))
print(check(["3 + 855", "380 - 2", "45 + 43", "123 + 49"], True))
print(check(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))