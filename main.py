from nessesary.matrix import Matrix
from nessesary.parser.parser import insert_mul_sign
from nessesary.polynomial import Polynomial
from nessesary.fraction import to_fraction
from file_read_write import *
from nessesary.equation.processing import change_side, poly_expand, simplify
import ast

def guide():
    while True:
        print("All of the command will be saved in history.json file.")
        print("====================== Command List ======================")
        print("1) solve[equation]: Solve equation and Polynomial")
        print("2) poly[str or list]: Solve Polynomial")
        print("3) Matrix[nested list]: Show all of that matrix property")
        print("4) det[equation]: Find Det")
        print("5) inverse[equation]: Find inverse matrix")
        print("6) tranpose[equation]: show the tranpose matrix")
        print("7) simplify[expression]: simplify the given expression")
        print("8) history: view history from history.json")
        print("9) clear: clear history.json")
        print("10) delete: delete history.json")
        print("11) guide: Open Guide file")
        print("12) q,quit: quit the program")

        print("========================== Guide ==========================")
        print("To use this program. type in the command and expression in form of")
        print("that command.")
        print("==========Syntax=========")
        print("""
        |    operator   |  meaning  |
        |:-------------:|:---------:|
        |       +       |    add    |
        |       -       | substract |
        | * or adjacant |  multiply |
        |       /       |  Division |
        |       ^       |   Power   |
        
        """)

        print("==========Example=========")
        print("[1]: solve[(2x-1)^2 = 0]")
        print("Input: (2x-1)^2=0")
        print("=========================")
        print("Solution to (2x-1)^2=0")
        print("Answer #1: x = -0.5 | x = -1/2")
        print("=========================")
        u_input = input("Type q to quit the help menu[q or quit]: ")
        try:
            if "q" in u_input.lower():
                break
        except:
            break


print("Calculator-for-Matrix-and-Algebra")
print("===================================")
print("Type 'Guide' or 'guide' to open guide menu")
print("===================================")
print("Type 'Quit' or 'q' to quit the program")
print("===================================")
line_count = 1
while True:
    command = input(f"[{line_count}]: ")
    try:
        brac_index = command.find("[")
        if brac_index != -1:
            todo = command[:brac_index]
            expr = command[brac_index+1:-1]
            temp1 = ''
            for i in expr:
                if i == " ":
                    temp1 += ""
                else:
                    temp1 += i
            expr = temp1
        else:
            if command.lower() in ["q", "quit", "quits"]:
                break
            elif 'clear' in command:
                clear()
                line_count += 1
                continue
            elif 'delete' in command:
                delete()
                line_count += 1
                continue
        if "histo" in command:
            read_history()
            line_count += 1
            continue
        if "guide" in command:
            guide()
            line_count += 1
            continue
        todo.lower()
    except:
        print("Invaid input. Please enter the input expression again.")
        command = None
        line_count += 1
        continue

    if "solve" in todo.lower():
        if "=" not in expr:
            try:
                val = ast.literal_eval(expr)
                poly = Polynomial(val)
            except:
                poly = Polynomial(expr)

        elif "=" in expr:
            new_expr = change_side(expr)
            try:
                poly = Polynomial(new_expr)
            except:
                sim_result = poly_expand(new_expr)
                poly = Polynomial(sim_result)

        print(f"Input: {expr}")
        print("="*(21+len(poly.to_str())))
        try:
            result_list = poly.solve()
            collected_answer = []
            counting = 1
            print(f"Solution to {expr}")
            for data in result_list:
                if data["imag"] == 0:
                    ans = data["real"]
                else:
                    if data["imag"] < 0:
                        ans = str(data["real"]) + "" + str(data["imag"]) + "i"
                    else:
                        ans = str(data["real"]) + "+" + str(data["imag"]) + "i"
                try:
                    print(f"Answer #{counting}: x = {ans} | x = {to_fraction(ans, reduce=True)}")
                except:
                    print(f"Answer #{counting}: x = {ans}")
                collected_answer.append(ans)
                counting += 1
            print("="*(21+len(poly.to_str())))
            write_command(todo, str(poly), collected_answer)
        except ValueError:
            print("Can't find solution to this expression.(Program can only find solution up too 2nd degree polynomial)")
            write_command(todo, str(poly), "")
            pass


    elif "poly" in todo.lower():
        try:
            val = ast.literal_eval(expr)
            poly = Polynomial(val)
        except:
            poly = Polynomial(expr)

        print(f"Input Polynoimial: {expr}")
        print("="*(21+len(poly.to_str())))
        try:
            result_list = poly.solve()
            collected_answer = []
            counting = 1
            print(f"Solution to {expr} = 0")
            for data in result_list:
                if data["imag"] == 0:
                    ans = data["real"]
                else:
                    if data["imag"] < 0:
                        ans = str(data["real"]) + "" + str(data["imag"]) + "i"
                    else:
                        ans = str(data["real"]) + "+" + str(data["imag"]) + "i"
                try:
                    print(f"Answer #{counting}: x = {ans} | x = {to_fraction(ans, reduce=True)}")
                except:
                    print(f"Answer #{counting}: x = {ans}")
                collected_answer.append(ans)
                counting += 1
            print("="*(21+len(poly.to_str())))
            write_command(todo, poly.to_str(), collected_answer)
        except ValueError:
            print("Can't find solution to this expression.(Program can only find solution up too 2nd degree polynomial)")
            write_command(todo, poly.to_str(), "")
            pass

    elif "eval" in todo.lower():
        try:
            expr = insert_mul_sign(expr)
            result = eval(expr)
            print(f"Result: {result}")
        except:
            raise ValueError("Error Occur!")

    elif "matrix" in todo.lower():
        colleted_dict = {}
        try:
            val = ast.literal_eval(expr)
            m1 = Matrix(val)
        except:
            print("invalid input.")
            line_count += 1
            continue
        print(f"Input Matrix: {m1}")
        try:
            print(f"Determinant: {m1.determinant()}")
            colleted_dict["det"] = m1.determinant()
        except:
            print(f"No determinant for {m1.row}x{m1.column} Matrix")
            colleted_dict["det"] = ""
        t_matrix = m1.tranpose()
        print(f"Tranpose Matrix: {t_matrix}")
        colleted_dict["tranpose"] = str(t_matrix)
        try:
            inv = m1.inverse()
            print(f"Inverse Matrix: {inv}")
            print("NOTE: inverse of matrix 3x3 4x4 ... is not the precise but 2x2 is precise.")
            colleted_dict["inverse"] = str(inv)
        except:
            print(f"Can't evaluate inverse of this matrix")
            colleted_dict["inverse"] = ""
        

    elif "det" in todo.lower():
        try:
            val = ast.literal_eval(expr)
            m1 = Matrix(val)
        except:
            print("invalid input.")
            line_count += 1
            continue
        try:
            print(f"Determinant: {m1.determinant()}")
            write_command(todo, str(m1), m1.determinant())
        except:
            print(f"No determinant for {m1.row}x{m1.column} Matrix")
            write_command(todo, str(m1), "")

    elif "inverse" in todo.lower():
        try:
            val = ast.literal_eval(expr)
            m1 = Matrix(val)
        except:
            print("invalid input.")
            line_count += 1
            continue
        try:
            inv = m1.inverse()
            print(f"Inverse Matrix: {inv}")
            print("NOTE: inverse of matrix 3x3 4x4 ... is not the precise but 2x2 is precise.")
            write_command(todo, str(m1), str(inv))
        except:
            print(f"Can't evaluate inverse of this matrix")
            write_command(todo, str(m1), "")

    elif "tranpose" in todo.lower():
        try:
            val = ast.literal_eval(expr)
            m1 = Matrix(val)
        except:
            print("invalid input.")
            line_count += 1
            continue
        try:
            tran = m1.tranpose()
            print(f"Tranpose Matrix: {tran}")
            write_command(todo, str(m1), tran)
        except:
            print(f"Error Occur! Please enter input again!")
            write_command(todo, str(m1), "")

    elif "sim" in todo.lower():
        try:
            print(f"Result of Simplify: {poly_expand(expr)}")
            write_command(todo, str(m1), poly_expand(expr))
        except:
            try:
                pass
            except:
                print("Can't simplify this expression.(maybe too many nested parentheless or Error in program.)")
                write_command(todo, str(m1), "")

    line_count += 1
    command = None
    todo = None
    expr = None