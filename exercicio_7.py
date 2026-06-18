def calculate_imc(patient_id: int | str , weight_kg: float | int ,  height_m: int | float)-> str | dict:

  """Função que é uma calculadora de IMC
    
    Args:
      patient_id (int | str) : Id único do usuário.
      weight_kg (float | int) : Peso do usuário.
      height_m (int | float) : Aultura do usuário.
  

    Returns:
      str: Uma mensagem de suceso para o usuário.
      dict: Salva os dados do usuário no banco de dados. 
  
  """

  data_base = {}
  
  try:
    if type(height_m) == str:
      height_m = height_m.replace(',','.')
    
    if type(weight_kg) == str:
     weight_kg =weight_kg.replace(',','.')
    
    height_m = float(height_m)
    weight_kg = float(weight_kg)
    
    if weight_kg > 0 and height_m > 0:
        resultado = weight_kg / (height_m ** 2)
        
        if resultado < 18.5:
          data_base.update({'patient_id':patient_id, 'imc':resultado, 'classification': 'Abaixo'})
          print('Você está abaixo do peso')
        
        elif resultado <= 24.9:
          data_base.update({'patient_id':patient_id, 'imc':resultado, 'classification': 'Normal'})
          print('Você está no peso Normal')
          
        elif resultado <= 29.9:
          data_base.update({'patient_id':patient_id, 'imc':resultado, 'classification':'SobrePeso' })
          print('Você está com SobrePeso')
        
        elif resultado > 30:
          data_base.update({'patient_id':patient_id, 'imc':resultado, 'classification':'Obesidade' })
          print('Você está com obesidade')
      
    else:
      print('Digite um número maior que 0')

  except ValueError:
    print('Digite um número válido')
    
  except TypeError:
    print('Digite um número válido')
          
  except Exception as e:
      print(f'Ocorreu um erro inesperado:{e}')
      
calculate_imc(1,'69','1,79') # Sucesso
calculate_imc(2,'62','1.79') # Sucesso
calculate_imc(3,62,1.79) # Sucesso
calculate_imc(4,'62','1.7a') # Mensagem de erro
calculate_imc(5,'6a','1.7a') # Mensagem de erro
calculate_imc(patient_id=6, weight_kg=95, height_m=1.75) # Sucesso



