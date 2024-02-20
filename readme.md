# Canvas Image Upload Service
This script utilizes the Canvas api to upload image files to a specified Canvas account's file system


## Configuration
The 'CanvasImageUploadService' class takes a single config object as a dependency. The config object requires the following params:


        'csv_file':"<Path to CSV data file>",
        'canvas_url':"<Your Canvas Base URL>",
        'access_token':"<Your Access Token Here>",
        'payload_path':"<Path to Directory Containing files to upload>"

