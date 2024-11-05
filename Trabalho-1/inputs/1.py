import random

# Função para verificar se uma string está na linguagem L
def is_in_language(string):
    count_a = string.count('a')
    count_b = string.count('b')
    count_c = string.count('c')

    # Verifica se as letras estão na ordem correta e se i * j == k
    if string == 'a' * count_a + 'b' * count_b + 'c' * count_c:
        return count_a * count_b == count_c
    return False

with open('/home/manu/Documents/ufsc/teoria-da-computacao/inputs/1.txt', 'w') as file:
    for _ in range(30):  # Alterar o número de inputs conforme necessário
        # Gera quantidades aleatórias de 'a', 'b' e 'c' que podem satisfazer a condição i * j = k
        count_a = random.randint(1, 5)
        count_b = random.randint(1, 5)
        count_c = count_a * count_b

        # Formata a string na ordem correta 'a^i b^j c^k'
        input_string = 'a' * count_a + 'b' * count_b + 'c' * count_c
        file.write(f"${input_string}$\n")

    for _ in range(30):  # Change the number of inputs as needed
        input_string = ''.join(random.choices(['a', 'b', 'c'], k=random.randint(1, 10)))  # Adjust the range of string length as needed
        file.write(f"${input_string}$\n")


# Ler os inputs do arquivo 1.txt e escrever as respostas no arquivo 1_ans.txt
with open('/home/manu/Documents/ufsc/teoria-da-computacao/inputs/1.txt', 'r') as input_file, \
        open('/home/manu/Documents/ufsc/teoria-da-computacao/inputs/1_ans.txt', 'w') as output_file:
    for line in input_file:
        input_string = line.strip()
        if is_in_language(input_string):
            output_file.write("sim\n")
        else:
            output_file.write("não\n")
