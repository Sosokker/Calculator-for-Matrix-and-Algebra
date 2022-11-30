from nessesary.matrix import Matrix
from file_read_write import *
import ast

print("Algebraic And Matrix Solving tools.")
print("===================================")
print("===============Guide===============")

line_count = 1
while True:
    command = input(f"[{line_count}]: ")
    
    brac_index = command.find("[")
    if brac_index != -1:
        todo = command[:brac_index]
        expr = command[brac_index+1:-1]

    else:
        if command.lower() in ["q", "quit", "quits"]:
            break
        elif command == "delete history":
            delete()

    if "solve" in todo.lower():
        pass

    elif "matrix" in todo.lower():
        val = ast.literal_eval(expr)
        m1 = Matrix(val)
        print(f"Input Matrix: {m1}")
        try:
            print(f"Determinant: {m1.determinant()}")
        except:
            print(f"No determinant for {m1.row}x{m1.column} Matrix")
        t_matrix = m1.tranpose()
        print(f"Tranpose Matrix: {t_matrix}")

    elif "det" in todo.lower():
        pass
    
    if brac_index != -1:
        save_dict = {todo:expr}
        read_write_command(save_dict)

    line_count += 1