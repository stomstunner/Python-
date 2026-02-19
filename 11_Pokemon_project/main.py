# first of all install requests module
# then we have to import request in our project

import requests

# 3. then we make the base url for connecting to the api
base_url = "https://pokeapi.co/api/v2/"

# 4. we make a defination for get the pokemenon information
def get_pokemeon_info(name):
    # 7. now we call the url with the dynamic url such as the base url and the parent object then the dynamic name of the pokemon from user
    url = f"{base_url}/pokemon/{name}"
    
    # 8. now we use the get method for getting the response from the url
    response = requests.get(url)
    # 9. now we can print the response from the api
    # print(response)
    # 10. <Response [200]>
    # here we get the response object 200 that is ok ..good our api is running  
    
    # 11. now we if else code for 
    if response.status_code == 200:
        # print("Data retrived!")
        # 12. we check that ki hamra data retrive ho rha hai toh ab ham usse json me convert kar denge jisse hame key value pair mil jaye
        # 13. aur usko ham ek varibale me store kar ke rakh lenge
        pokemon_data = response.json()
        # print(pokemon_data)
        # 14. now we return this pokemon data to where it being called
        
        return pokemon_data
        
    else:
        print(f"Failed to retrive the data {response.status_code}")

# 5. now we want a name of the pokemon than we get from user of hardcode
# ===================================
pokemon_name = "Pikachu"

# 6. now we call the definition
# 15. now we store the infrmation from the api to a variable

pokemon_info = get_pokemeon_info(pokemon_name)

# 17. now we check that ki hamra pokemon_info me kuch value hai ki nahi ager hoga toh ham uske ander me se kuch data to print karwa denge
if pokemon_info:
    
    # 18. ab ham usko print karne ka try karnege but hamra result ek dictinory me hai toh hame formated string ke ander curlly braket uske kar ke resultant vaibale ke naam likh ke uske me se list wla [] baraket ke ander key ka naam as a string me likhna hoga
    # print(pokemon_info)
    print(f"The name of the Pokemon is : {pokemon_info["name"].capitalize()}")
    # if want ki hamre resultant string ka first letter capital me ho toh hame resultant string ke aage dot and capitalize() method ka use karna hoga 
    print(f"The id of the Pokemon is : {pokemon_info["id"]}")
    print(f"The height of the Pokemon is : {pokemon_info["height"]} feet")
    print(f"The weight of the Pokemon is : {pokemon_info["weight"]} pounds")