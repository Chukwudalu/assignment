from flask import Flask, request, Response
import json
from pathlib import Path

app = Flask(__name__)

json_folder = Path("data")
all_transcripts = Path("data/transcripts.json")

def merge_files():
    """
        get all the data from each json file.
        append each to a list
        Write all to a neew file as a json object 

        Parameters -> None
        Returns -> None
    """
    
    transcripts = []
    try:
        for json_file in json_folder.glob("*.json"):
            with open(json_file, 'r') as file:
                data = json.load(file)
                transcripts.append(data)

        if not all_transcripts.exists():
            all_transcripts.write_text(json.dumps(transcripts, indent=4))

    except ValueError as error:
        print (error)

merge_files()


@app.get('/')
def get_all():
    """
       This function returns all trascripts 

       Parameters -> None
       Returns -> all transcipts 
    """
    try:
        with open("data/transcripts.json", "r") as file:
            data = json.load(file)

        return Response(json.dumps(data), 200)
    
    except (ValueError, json.JSONDecodeError, FileNotFoundError):
        return Response(json.dumps({"message": "An error occured"}), 500)


@app.get('/<int:id>')
def get_by_id(id):
    """
        This function converts the transcript from json to a dictionary and returns 
        the transcript that has the transcript with matching id.

        Parameters -> transcript_id
        Returns -> transcript
    """
    with open("data/transcripts.json", "r") as file:
        data = json.load(file)

        for transcript in data:
            if int(transcript["transcript_id"]) == id:
                return Response(json.dumps(transcript), 200)
            
        return Response(json.dumps({"message": "transcript not found"}), 404)

@app.put('/edit')
def edit():
    """
        This function updates a transcript if it already exists. If not,
        it creates a new one

        Parameters -> none
        Returns -> status message
    """
    transcript = request.get_json()
    try:
        with open("data/transcripts.json", "r") as file:
            data = json.load(file)
            for d in data:
                # if matching id, update database
                if d["transcript_id"] == transcript["transcript_id"]:
                    print(d["transcript_id"], transcript["transcript_id"])
                    for key, value in transcript.items():
                        d[key] = value
                    all_transcripts.write_text(json.dumps(data, indent=4))
                    return Response(json.dumps({"message":"success"}), 200)

            # if the transcripts folder isn't updated due to no mathing id, a new transcript is created  
            data.append(transcript)
            all_transcripts.write_text(json.dumps(data, indent=4))
            return Response(json.dumps({"message":"success"}), 201) 
            
    except (ValueError, json.JSONDecodeError, FileNotFoundError):
        return Response(json.dumps({"message":"An error occured in the server. Please try again later"}), 500)



if __name__ == '__main__':
    app.run(debug=True)
        
    