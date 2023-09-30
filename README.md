# BoardCardSorter
To clone and run a Django app, you'll need the following prerequisites:

    1. Python: Django is a Python web framework, so you need Python installed on your system. 
    2. Virtual Environment (Optional): It's a good practice to create a virtual environment for your Django project. This isolates your project's dependencies from the system-wide Python installation.
    
Step 1: First you have to clone the repository using given below command:
            git clone https://github.com/OmParkash1996/BoardCardSorter.git

Step 2: You can install this project requirments through following command:

pip install -r requirements.txt

After that you have to run the server through following commands:

python manage.py runserver


Following below is the end_point, input and output parameters,
   
    endpoint: api/boarding-cards/
    description: It will return the description of how to complete your journey
    request_type: POST
    input: [
              {
                  "departure": "Madrid",
                  "arrival": "Barcelona",
                  "transportation": "train 78A",
                  "seat": "45B"
              },
              {
                  "departure": "Barcelona",
                  "arrival": "Gerona Airport",
                  "transportation": "airport bus"
              },
              {
                  "departure": "Gerona Airport",
                  "arrival": "Stockholm",
                  "transportation": "flight SK455",
                  "gate": "45B",
                  "seat": "3A",
                  "additional_info": "Baggage drop at ticket counter 344."
              },
              {
                  "departure": "Stockholm",
                  "arrival": "New York JFK",
                  "transportation": "flight SK22",
                  "gate": "22",
                  "seat": "7B",
                  "additional_info": "Baggage will be automatically transferred from your last leg."
              }
            ]

    output: {
                "sorted_boarding_cards": [
                    "1. Take train 78A from Madrid to Barcelona. Sit in seat 45B.",
                    "2. Take airport bus from Barcelona to Gerona Airport.",
                    "3. Take flight SK455 from Gerona Airport to Stockholm. Gate 45B. Sit in seat 3A. Baggage drop at ticket counter 344.",
                    "4. Take flight SK22 from Stockholm to New York JFK. Gate 22. Sit in seat 7B. Baggage will be automatically transferred from your last leg.",
                    "5. You have arrived at your final destination."
                ]
            }
