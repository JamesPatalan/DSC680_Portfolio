import openai
import json
import requests

with open(r"C:\Users\User\School\Set5\OpenAI_Key.json") as file:
    keys = json.load(file)
    OAI_Key = keys['Key']

openai.api_key = OAI_Key


def chat(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content']


def get_restaurants(api_key, location, term='restaurants', food_type=None):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer ' + api_key}

    params = {'term': term, 'location': location, 'sort_by': 'rating', 'limit': 5}
    if food_type:
        params['categories'] = food_type

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        businesses = data.get('businesses', [])
        if businesses:
            # Format the response with top-rated restaurants
            result = "Here are the top-rated {} in {}: \n".format(term, location)
            for i, business in enumerate(businesses, start=1):
                result += "{}. {} - Rating: {} \n".format(i, business['name'], business['rating'])
            return result
        else:
            return "No {} found in {}".format(term, location)
    else:
        print("Failed to retrieve data from Yelp API.")
        return None

def main():
    with open(r"C:\Users\User\School\Set5\YelpAPI_Key.json") as file:
        keys = json.load(file)
        API_Key = keys['Key']

    location = 'Orlando, FL'

    print('What food can I help you find?')
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

        food_type = user_input

        response = chat(user_input)
        print("ChatEAT:", response)
        restaurant_results = get_restaurants(API_Key, location, food_type=food_type)
        print("ChatEAT:", restaurant_results)
        response_2 = chat(restaurant_results)
        print("ChatEAT:", response_2)

if __name__ == '__main__':
    main()
