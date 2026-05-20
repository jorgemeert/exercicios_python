#VALIDADOR DE CPF 

def iniciar():
  print('\nBem vindo ao Validador de CPF')
  str_cpf = input('Digite seu cpf para verificação').replace('.','').replace('-','')
  return str_cpf
data_base = {}
user_id = 1
str_cpf = ''


def validate_cpf(user_id: int, str_cpf: int) -> str | dict:
      """ Função que verifica se o CPF é validado

          Funçaõ recebe um valor que é o cpf, esse cpf entra no while e
          só sai quando o usuário inputa um valor que seja válido
      
          
          Args:
            str_cpf (int,str) : CPF
            
          
          Returns:
            str : Printa um mensagem de sucesso!
            dict: Salva os dados no dicionário
          
          
      """  
      
      cpf =''
      while len(str(cpf)) != 11:
          str_cpf = iniciar()
          try:
            cpf = int(str_cpf)
            if len(str(cpf)) != 11:
                print('O CPF precisa ter 11 dígitos, tente novamente:')
          except ValueError:
            print('Você está digitando um valor inválido')

          except Exception as e:
            print(f'Ocorreu um erro inesperado: {e}')
      
      print('\n\nTudo certo! CPF verificado com sucesso!')
      data_base.update({'user_id' : user_id,'cpf' : cpf})
  

validate_cpf(user_id,str_cpf)

