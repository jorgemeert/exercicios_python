from datetime import date


def validate_card(user_id : int | str , card_number : int ,expiry_date : int) -> str | dict:
  
  """Função que válida o cartão de crédito, verifica a quantidade de números no cartão e se eles está vencido.
  
    Args:
      user_id(int | str ): ID do usuário
      card_number(int): Número do cartão
      expiry_date(int): Data de vencimento do cartão
      
    Returns:
      str: Mensagem de erro ou de falha.
      dict: Caso, esteja tudo certo, salva no banco de dados.
  
  
  """
  data_base = {}
  
  try:

      hoje = date.today()
      card_number = str(card_number).strip()
      expiry_date = expiry_date.replace('-','/')
      expiry_date = expiry_date.split('/')

      if len(card_number) == 16:
        if len(expiry_date) == 2 and int(card_number):
          if int(expiry_date[1]) > hoje.year:
            print("Cartão válido")
            data_base.update({'user_id':user_id,'expiry_date':expiry_date,'card_number':card_number, 'status' : 'válido'})
      
          else:
            if int(expiry_date[1]) == hoje.year and int(expiry_date[0]) >= hoje.month:
              print("Cartão válido")
              data_base.update({'user_id':user_id,'expiry_date':expiry_date,'card_number':card_number, 'status' : 'válido'})
            else:
                print('Seu cartão está vencido, contate seu Banco para renovação!')
        
        else:
          print('Digite apenas o mês e o ano do vencimento do seu cartão!')
          
      else:
        print('Digite um cartão válido (16 digitos)')
        
  except ValueError:
    print('Digite valores válidos!')
      
  except AttributeError:
    print('Digite um mês e ano válido!')
    
  except Exception as e:
      print("Ocorreu um erro inesperado: {e}")

validate_card(1,'1234267891022131','06-2026' ) # TUDO CERTO
validate_card(1,'1234267891022131','12/2027') # TUDO CERTO
validate_card(1,'1234267891022131',2) # MENSAGEM DE ERRO
validate_card(1,'123426789102','12-2026') # MENSAGEM DE ERRO 
validate_card(1,'12342678910221AA','12/2028') # MENSAGEM DE ERRO
validate_card(1,'12342678910221322221','10-2012') # MENSAGEM DE ERRO


