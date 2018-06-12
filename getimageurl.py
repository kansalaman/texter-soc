from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()
query=input('Enter Query: ')  #class instantiation

arguments = {"keywords":query,"limit":2,"print_urls":False}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images
