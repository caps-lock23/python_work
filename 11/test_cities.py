from city_functions import location

def test_city_country():
    formatted_city = location('manila', 'philippines')
    assert formatted_city == 'Manila, Philippines'

def test_city_country_population():
    formatted_city = location('manila', 'philippines', '500000')
    assert formatted_city == 'Manila, Philippines - Population 500000'