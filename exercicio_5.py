def check_plate(vehicle_id: int | str , plate: int | str) -> str | dict:
    """"""

    format = ''
    data_base = {}
    try:
        plate = str(plate.upper().replace(' ',''))

        if len(plate) == 7:
            if plate[0].isalpha() and plate[1].isalpha() and plate[2].isalpha():
                if plate[3].isdigit() and plate[4].isdigit() and plate[5].isdigit() and plate[6].isdigit():
                    format = 'Modelo antigo'
                    data_base.update({'vehicle_id':vehicle_id,'plate':plate,'format':format})
                    print(f'Sua placa "{plate}" é o modelo antigo')

                elif plate[3].isdigit() and plate[4].isalpha() and plate[5].isdigit() and plate[6].isdigit():
                    format = 'Mercosul'
                    data_base.update({'vehicle_id':vehicle_id,'plate':plate,'format':format})
                    print(f'Sua placa "{plate}" é o modelo antigo')

            else:
                print('A placa que você passou não é uma placa verdadeira!')

        else:
            print('Sua placa precisa ter 7 caracteres')

    except AttributeError:
        print('Sua placa precisa conter letras')


check_plate(1,'asd123')
