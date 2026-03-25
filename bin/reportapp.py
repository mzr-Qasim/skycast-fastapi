import requests

def main():

    choice = input("[R]eport weather or [s]ee reports?")

    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"dont know what to do with {choice}")
        
        choice = input("[R]eport weather or [s]ee reports?")



def report_event():
    desc = input("What is happening now ?")
    city= input("What city ?")
    data = {
        "description" : desc,
        "location" : {
            "city" : city

        }


    }
    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    print(data)


    # for r in data:
    #     print(f"{r.get('location').get('city')} has {r.get('description')} ")

    # """
    # {
    #     "description" : "Saw a little flooding.",
    #     "location" : {
    #         "city" : "RWP",
    #         "state" : "OR",
    #         "country": "PAK"

    #     },
    #     "id" : "1234-5678-9101",
    #     "created_date" : "2020-11-04T08:57:31:082590"

    # },
    # {
    #     "description" : "Saw a little Rain.",
    #     "location" : {
    #         "city" : "RWP",
    #         "state" : "OR",
    #         "country": "PAK"

    #     },
    #     "id" : "1234-5678-9102",
    #     "created_date" : "2020-11-04T08:59:31:082593"

    # }
    # """



if __name__ == '__main__':
    main()