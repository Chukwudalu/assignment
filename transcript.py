import requests
import json

class Transcript:
    def __init__(self):
        self.server_base_url = "http://localhost:5000/"
        self.transcript_cache = []
        self.get_all()
    

    
    def get_all(self):
        """
            gets all the transcript data from the server
            parameters -> None
        """
        try:
            response = requests.get(self.server_base_url, timeout=6)
            response.raise_for_status()
            data = response.json()

            for d in data:
                if len(self.transcript_cache  ) == 0:
                    self.transcript_cache.append(d)
                    continue
                inserted = False
                for i in range(len(self.transcript_cache)):
                    if int(d["transcript_id"]) < int(self.transcript_cache[i]["transcript_id"]):
                        self.transcript_cache.insert(i, d)
                        inserted = True
                        break
                
                if inserted == False:
                    self.transcript_cache.append(d)
            
            # print(f"\n{self.transcript_cache}\n")
            
        except requests.exceptions.HTTPError:
            status_code = str(response.status_code)
            if status_code.startswith("5"):
                print("An error occured in the server, please try again later.")
            elif status_code.startswith("4"):
                print("please check your request response and try again")
        except requests.exceptions.Timeout as e:
            print("Reqest timed out. Please try again")
        except requests.exceptions.RequestException as e:
            print("An unexpected error occured. Please try again")



    def choose_student(self, transcript_id):
        """
            Lets user selects a specific transcript to view

            Parameters -> transcript_id
        """
        try:
            if not int(transcript_id):
                raise ValueError
            else:
                
                response = requests.get(f"{self.server_base_url}/{transcript_id}")
                response.raise_for_status()
                return response.json()
               

        except ValueError as e:
            print("Your input cannot be a transcript id. Please try again")
        
        except requests.exceptions.HTTPError:
            status_code = str(response.status_code)
            if status_code.startswith("5"):
                print("An error occured in the server, please try again later.")
            elif status_code.startswith("4"):
                print("please check your request data and try again")
        except requests.exceptions.Timeout as e:
            print("Reqest timed out. Please try again")
        except requests.exceptions.RequestException as e:
            print("An unexpected error occured. Please try again")


    def edit_transcript(self, data):
        """
            Lets user edit a specific transcript in the database

            Parameter -> transcript
        """
        try:
            response = requests.put(f"{self.server_base_url}/edit", json=data)
            response.raise_for_status()
            print("Transcript updated")
        except requests.exceptions.HTTPError:
            status_code = str(response.status_code)
            if status_code.startswith("5"):
                print("An error occured in the server, please try again later.")
            elif status_code.startswith("4"):
                print("please check your request data and try again")
        except requests.exceptions.Timeout as e:
            print("Reqest timed out. Please try again")
        except requests.exceptions.RequestException as e:
            print("An unexpected error occured. Please try again")

    
