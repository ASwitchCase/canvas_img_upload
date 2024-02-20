import csv,requests,os


test_config = {
    "csv_file":"user_img_data.csv",
    "canvas_url":"<Your Canvas URL>",
    "access_token":"<Your Access Token Here>",
    "payload_path":"images/"
}

class CanvasImageUploadService():
    def __init__(self,config):
        self.config = config
    
    def csv_to_json(self):
        result = {"data":[]}
        with open(self.config["csv_file"]) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                # row[0] = user_id row[1] = file_name row[2]: file_type
                result["data"].append({
                    "user_id":row[0],
                    "file_name":row[1],
                    "file_type":row[2]
                })
        return result
    
    def get_upload_request(self,user_obj):
        header = {'Authorization':f'Bearer {self.config["access_token"]}'}
        url_params = {
            'name': user_obj["file_name"],
            'size': os.path.getsize(f'./{self.config["payload_path"]}{user_obj["file_name"]}'),
            'content_type':f'image/{user_obj["file_type"]}',
            'parent_folder_path':'profile_pictures',
        }

        return {"header":header,"url_params":url_params}
    
    def bulk_upload(self,users):
        for user in users:

            if user["file_name"] == "file_name":
                continue

            req = self.get_upload_request(user)
            res = requests.post(
                url=f"{self.config["canvas_url"]}api/v1/users/self/files",
                headers=req["header"],
                data=req["url_params"]
            )
            json_res = res.json()
            files = {'file':open(f'./images/{user["file_name"]}','rb').read()}

            upload_file_response = requests.post(json_res['upload_url'],data=json_res["upload_params"],files=files,allow_redirects=False)
    
    def run(self):
        users = self.csv_to_json()["data"]
        self.bulk_upload(users)






canvas = CanvasImageUploadService(test_config)
canvas.run()
