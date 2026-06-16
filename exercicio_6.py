from datetime import date
 
def validate_card(user_id,card_number,expiry_date):

  hoje = date.today()
  card_number = str(card_number).strip()
  expiry_date = expiry_date.split('/')
  
  
  if len(card_number) == 16:
    if len(expiry_date) == 2:
      if int(expiry_date[0]) != hoje.month or int(expiry_date[1]) > hoje.year:
        print("Cartão válido")
  
      else:
        print('Seu cartão está vencido, contate seu Banco para renovação!')
    
    else:
      print('Digite apenas o mês e o ano do vencimento do seu cartão!')
      
  else:
    print('Digite um cartão válido (16 digitos)')

validate_card(1,1234567891022131,'06/2027',)