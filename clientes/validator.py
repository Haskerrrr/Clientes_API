def cpf_valid(num_cpf):
    return len(num_cpf) == 11

def nome_valid(nome):
    return nome.isalpha()

def rg_valid(num_rg):
    return len(num_rg) != 9

def celular_valid(num_celular):
    return len(num_celular) < 11