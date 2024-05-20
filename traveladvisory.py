

import requests
import json




def get_country_info(country_code):
    url = f"https://www.travel-advisory.info/api"
    response = requests.get(url)
    data = response.json()
    return data

def write_to_json(data, data_json_info):
    with open(data_json_info, 'w') as file:
        json.dump(data, file, indent=4)


def print_country_info(data):
    if "data" in data and len(data["data"]) > 0:
        country = data["data"][0]
        print(f"Country: {country['name']}")
        print(f"ISO Alpha2: {country['iso_alpha2']}")
        print(f"Continent: {country['continent']}")
        print(f"Advisory Score: {country['Advisory']['score']}")
        print(f"Advisory Message: {country['Advisory']['message']}")
    else:
        print("No data available")

def main():
    country_code = input("Enter a two-letter ISO country code: ")
    data = get_country_info(country_code)
    write_to_json(data, f"{country_code}.json")
    print_country_info(data)

if __name__ == "__main__":
    main()




# <section>
#     {% include "mytravel/included/traveladvice/search_and_filterbar.html" %}
#   </section>

#   <section>
#     <form action="." method="post">
#       {%csrf_token%}
#       <label for="country">Enter your destination country (ISO code):</label>
#       <input type="text" id="country" name="country">
#       <button type="submit">Get Travel Advisory</button>
#     </form>
#   </section>

# <div class="row">
#         <div class="col-lg-8">          
#           <div class="flight-custom-card">
#               <a href=""> <img  class="img-fluid mb-4" src="{{advice.image.url}}" alt=""/></a>
#               <ul class="list-inline small text-uppercase mb-0">
#                 <!-- <li class="list-inline-item mr-0 text-gray align-middle">By </li> -->
#                 <!-- <li class="list-inline-item align-middle mr-0"><a class="font-weight-bold reset-anchor" href="#">{{advice.author}}</a></li> -->
                
#                 <!-- <li class="list-inline-item text-gray align-middle mr-0">|</li> -->
#                 <!-- <li class="list-inline-item text-gray align-middle">{{advice.updated_at|timesince}} ago</li> -->
#               </ul>

#                 <div class="">
#                   <h4>Travel Advisory for {{ advisory_info.country }}</h4>

                    
                
#                   <p>Advisory Score: {{ advisory_info.advisory_score }}</p>

                 
        
#                   <p>Advisory Message: {{ advisory_info.advisory_message }}</p>

      
#                 </div>
#             </div>
        

#         </div>

#       </div>
      
#     <h1>Travel Advisory for {{ advisory_info.country }}</h1>
#     <p>Advisory Score: {{ advisory_info.advisory_score }}</p>
#     <p>Advisory Message: {{ advisory_info.advisory_message }}</p>

#     {% block API_content %}

#     {% endblock %}

#     <!-- **************************APIcontentblock ends**************************** -->

        