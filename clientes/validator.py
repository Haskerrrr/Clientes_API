import re
from validate_docbr import CPF

def cpf_valid(num_cpf):
    cpf = CPF()
    return cpf.validate(num_cpf)

def nome_valid(nome):
    return nome.isalpha()

def rg_valid(num_rg):
    return len(num_rg) != 9

def celular_valid(num_celular):
    """ Verifica se o celualr é valido 00 0000-0000"""
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, num_celular)
    return resposta