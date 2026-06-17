def calculate_imc(patient_id,weight_kg, height_m):
  data_base = {}
  
  
  if weight_kg > 0 and height_m > 0:
    resultado = weight_kg / (height_m * 2)
    
    if resultado < 18.5:
      print(resultado)
      print('abaixo do peso')
    
    elif resultado >= 18.5:
      print(resultado)
      print('Normal')
      
    elif resultado >= 25:
      print(resultado)
      print('SobrePeso')
    
    elif resultado > 30:
      print(resultado)
      print('obesidade')
      
      
calculate_imc(1,69,1.10)