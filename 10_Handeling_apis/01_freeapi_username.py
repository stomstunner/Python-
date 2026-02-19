# in this program we learn about how to handle application program interface(api)

import requests

# now we make a defination that help us to fetch random user from free api

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    
    # now we use the requests features like get,post and many more
    # first of all we use the get method where we pass the url(variable that we have)
    
    response = requests.get(url)
    # we use the json formate because the data receved from the server by api is in the string formate so if we want to use it efficently then we have to convert it in the json formate  
    # we can apply the json formate by just using the dot operator wiht response because the response it the variable holds all the comming data 
    data = response.json()
    
    # now we write the code for checking the data is comming or not
    # ki hamare data vaiable me kya success hai aur kya data hai data object me 
    if data["success"] and "data" in data:
        user_data = data["data"]
        # now we want ki hame user_data me jo data ke data ka pura object store hai us me se login me jaa ke username fetch kar ke lana hai
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    
    # now we write the else case where we raise a exception
    # raise is use to show the error
    else:
        raise Exception("Failed to fetch user data")
    

# lets write the main function
def main():
    # ho skata hai ki hamra main fucntion hi crach ho jaye toh uske liye hai try and catch ka use karna haga
    
    try:
        # ab ham yaha pass me kuch nahi karenge bass apne method ko call kar denge 
        username, country = fetch_random_user_freeapi()
        # now we just print these username and county in a formated string
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))
        #ho sakt hai ki hamra exception ko ager formate me aaya hua hai toh usko ham string me hi convert karne ke baad hi print karenge 
        
        
# lets write the dunder part
if __name__ == "__main__":
    main()