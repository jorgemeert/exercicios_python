def validate_email(user_id: int | str ,email: str) -> str | dict:
  
  """Função que valida o email do usuário e salva no banco de dados
  
    Args:
      user_id(int | str): ID do usuário
      email(str): email do usuário
    
    Returns:
      str: Mensagem de erro ou sucesso
      dict: Caso haja sucesso, salva em um dicionário
  
  
  """
  
  data_base = {}
  
  try:
      if '@' in email:
        if email.count('@') == 1:
          verify_email = email.split('@')
          if '.' in verify_email[1]:
            if ' ' not in email:
              verify_domain = verify_email[1].split('.')
              if len(verify_domain[-1]) >= 2:
                data_base.update({'user_id' : user_id, 'email': email})
                print('Email válido!')

              else:
                print('Domínio incorreto, o domínio precisa ter no mínimo 2 caracteres.')
              
            else:
              print('O email contém espaços!')
            
          else:
            print('Depois do "@" o email precisa de pelo menos 1 ponto para o domínio')
          
        else:
          print('Email pode conter apenas 1 "@"')
      else:
        print('O email precisa ter "@"')
        
  except TypeError:
    print('Digite uma string no email')
        
  except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')    
     
validate_email(1,'jorgeflmrt@gmail.com') #sucesso
validate_email(2,'jorgeflmrt@@gmail.com') #erro 
validate_email(3,'jorgeflmrt@gmail.com.br') #sucesso
validate_email(4,'jorgef.lmrt@gmail.com') #sucesso
validate_email(5,'jorgeflmrt@gmail.m') #erro
validate_email(6,'jorgeflmrt@gmailcom') #erro
validate_email(7,'jorgeflm rt@gmail.com') #erro








