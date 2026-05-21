def calculate_shipping(order_id: int | str,weight_kg: float | int, distance_km: float | int)-> str | dict:
  
  """ Função que calcula o frete de acordo com o peso e distância
  
      Args:
        order_id (int | str): ID do usuário.
        weight_kg (int | float): Peso do produto que irá ser enviado.
        distance_km (int | float): Distância em km.
        
        
      Returns:
        str: Envia uma mensagem para o usuário de sucesso ou erro.
        dict: Salva os dados do usuário em um dicionário. 
  
  """
  data_base = {}
  try:  
      if weight_kg > 0 and distance_km > 0:  
        value_kg = 2 * float(weight_kg)
        value_km = 0.5 * float(distance_km)
        shopping_cost = value_kg + value_km
        data_base.update({'order_id':order_id,'weight_kg':weight_kg,'distance_km': distance_km,'shopping_cost':shopping_cost})
        print(f'\n\nA distância do envio é {data_base['distance_km']}Km e o peso é {data_base['weight_kg']}KG, portando o valor do envio é {data_base['shopping_cost']}\n\n')

      else:
        print('Coloque um valor Positivo nos campos!')
  
  
  except TypeError:
    print('Valor incorreto, nos valores digite apenas números!')
    
    

    
calculate_shipping(order_id=1,weight_kg=12,distance_km=1) # SUCESSO
calculate_shipping(order_id=1,weight_kg='abv',distance_km=1)# Mensagem de erro.

calculate_shipping(order_id=1,weight_kg=-3,distance_km=1)# Mensagem de erro, aceitando apenas números posistivos.