def car_info(manufacturer, model, **info):
    info['manufacturer'] = manufacturer
    info['model'] = model
    
    return info

print(car_info('rusi', 'de atras', color = 'black', reverse = True))
