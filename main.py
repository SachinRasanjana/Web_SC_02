from bs4 import BeautifulSoup
import requests

address_01 = 'https://ikman.lk'
flag = True
page = 1

while flag:

    address = "https://ikman.lk/en/ads/sri-lanka/cars?sort=date&order=desc&buy_now=0&urgent=0&page="+str(page)
    page += 1
    html_txt = requests.get(address).text
    soup = BeautifulSoup(html_txt, "lxml");
    cars = soup.find_all("li", class_="normal--2QYVk gtm-normal-ad")

    for car in cars:

        value_list = []
        details_list = []
        both_val = {}

        car_time = str(car.find('div', class_='updated-time--1DbCk').text)
        car_link = car.a["href"]
        address_02 = address_01+car_link
        inside_text = requests.get(address_02).text
        soup2 = BeautifulSoup(inside_text, "lxml")

        car_details = soup2.find_all('div', class_='word-break--2nyVq value--1lKHt')
        car_label = soup2.find_all('div', class_='word-break--2nyVq label--3oVZK')

        if car_time == "2 days":
            flag = False
            break

        for label in car_label:
            value_list.append(label.text)

        for car_01 in car_details:
            details_list.append(car_01.text)

        car_price = soup2.find('div', class_='amount--3NTpl').text
        # car_brand = details_list[0]
        # car_model = details_list[1]
        # car_year = details_list[3]
        # car_condition = details_list[4]
        # car_transmission = details_list[5]
        # car_bodyType = details_list[6]
        # car_fuelType = details_list[7]
        # car_engineCapacity = details_list[8]
        # car_mileage = details_list[9]

        # print(f'''
        # Car Brand: {car_brand}
        # Car Price: {car_price}
        # Car Time: {car_time}
        # Car Model: {car_model}
        # Car Year: {car_year}
        # Car Condition: {car_condition}
        # Car Transmission: {car_transmission}
        # Car Body Type: {car_bodyType}
        # Car Fuel Type: {car_fuelType}
        # Car Engine Capacity: {car_engineCapacity}
        # Car Mileage:
        #
        # Link : {address_02}
        # ''')

        for i in range(len(value_list)):
            both_val[value_list[i]] = details_list[i]

        print(car_time)
        print(car_price)
        print(address_02)
        for c_key, c_value in both_val.items():
            print(c_key, c_value)
        print("______________________________")
print("End")
