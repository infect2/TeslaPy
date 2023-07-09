import teslapy
with teslapy.Tesla('infect2@hanmail.net') as tesla:
    vehicles = tesla.vehicle_list()
    print(vehicles)
    vehicles[0].sync_wake_up()
    vehicles[0].get_vehicle_data()
    print(vehicles[0]['vehicle_state']['car_version'])
    print(vehicles[0])
    # 보험에 가입이 안되어 있어서 오류가 나는 것으로 보임
    # url = 'https://akamai-apigateway-vfx.tesla.com/safety-rating/daily-metrics'
    # print(tesla.get(url, params={'vin': vehicles[0]['vin'], 'deviceLanguage': 'kor',
    #                              'deviceCountry': 'KOR', 'timezone': 'KTC'}))
    # Tesla 제어 명령 보내기
    try:
        vehicles[0].command('ACTUATE_TRUNK', which_trunk='rear')
    except teslapy.HTTPError as e:
        print(e)
    # try:
    #     vehicles[0].command('UNLOCK')
    # except teslapy.HTTPError as e:
    #     print(e)
