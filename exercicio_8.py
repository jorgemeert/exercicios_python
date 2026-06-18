def apply_discount(order_id : int | str , price: int | float, coupon: str) -> str | dict:

  """Função que válida cupons, e apresentar os valores finais com os cupons
  
    Args:
      order_id(int | str): Id único do usuário.
      price( int | float ): Preço do produto do usuário.
      coupon(str) : O cupom para o desconto.
      
    Returns:
      str: Mensagem para o usuário,
      dict: Dados do usário salvo no banco de dados.
  
  """
  
  data_base = {}
  descontos = {
    'CUPOM70' : 70,'VEMPRACOPA20' : 20,'BRASIL15':15,
    'PRIMEIRACOMPRA' :50
  }
  try:
      if type(price) == str:
        price = price.replace(',','.')

      price = float(price)
      coupon = coupon.upper()

      if price > 0:
        if coupon in descontos:
          valor = descontos[coupon]
          desconto = (price  * valor) / 100
          final_price = price - desconto
          
          data_base.update({'order_id' : order_id, 'original' : price, 'discount' : valor, 'final_price':final_price})
          
          print(f'Sua compra de {price} com o cupom : {coupon} teve desconto de {valor}% e o preço final ficou {final_price}')

        else:
          print('Infelizmente o cupom que você digitou está incorreto')  

      else:
        print('Digite um valor positivo') 
        
  except AttributeError:
    print('Digite valores válidos.')
    
  except Exception as e:
    print(f'Ocorreu um erro inesperado : {e}')
    
apply_discount(1,50,'BRASIL15') # Sucesso.
apply_discount(2,'50','BRASIL15') # Sucesso.
apply_discount(3,-50,'BRASIL15') # Mensagem de erro.
apply_discount(4,'a','BRASIL15') # Mensagem de erro.
apply_discount(5,100,'BRASIL') # Mensagem de erro.
apply_discount(6,3,'Cumpom') # Mensagem de erro.