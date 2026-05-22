def register_temperature(sensor_id: int | str, temperature: float | int) -> str | dict:
    """ Função que verifica a temperatura e diz o stats dela

        Args:
            sensor_id (int | str): ID do sensor.
            temperature (int | float): Temperatura.

        Returns:
            str: Dá uma mensagem do status da temperatura.
            dict: Salva no banco de dados o sensor_id, temperature, status.

    """

    data_base = {}
    status = ''
    try:
        if type(temperature) == str and ',' in temperature:
            temperature = temperature.replace(',','.')
        temperature = float(temperature)
    except ValueError:
        print('Digite um temperatura com números')
        return
    if type(temperature) == float:
        if temperature >= -50 and temperature <= 60:
            if temperature <= 15:
                status = 'Frio'
                data_base.update({'sensor_id':sensor_id,'temperature':temperature,'status':status})
                print('frio')

            elif temperature > 15 and temperature <= 28:
                status = 'Agradável'
                data_base.update({'sensor_id':sensor_id,'temperature':temperature,'status':status})
                print('Agradável')

            else:
                status = 'Quente'
                data_base.update({'sensor_id':sensor_id,'temperature':temperature,'status':status})
                print('Quente')

        else:
                print('Digite um temperatura entre -50 a 60')




register_temperature(sensor_id= 1,temperature='asdaad') #Erro
register_temperature(sensor_id= 2,temperature='12') #Frio
register_temperature(sensor_id= 3,temperature='32,3') #Quente
register_temperature(sensor_id= 4,temperature='23.4') #Agradável
register_temperature(sensor_id= 5,temperature=-30) #Frio
register_temperature(sensor_id= 6,temperature=-80) #Erro
register_temperature(sensor_id= 7,temperature=80) #Erro






