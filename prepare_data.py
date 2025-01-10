import os
import tarfile
import requests

cwd = os.path.join(os.getcwd(),"fortiface_ai\data",)
# setup paths
pos_path = os.path.join(cwd,"pos")
neg_path = os.path.join(cwd,"neg")
anc_path = os.path.join(cwd,"anc")

# make directories
os.makedirs(pos_path,exist_ok=True)
os.makedirs(neg_path,exist_ok=True)
os.makedirs(anc_path,exist_ok=True)
print(cwd)

def download_data(url,cwd):
    os.makedirs(cwd,exist_ok=True)
    tarfile_path = os.path.join(cwd,"lfw.tar")
    with requests.get(url, stream=True) as response:
        response.raise_for_status()  # Raise an error for HTTP issues
        with open(tarfile_path, "wb") as tar_file:
            for chunk in response.iter_content(chunk_size=8192):
                tar_file.write(chunk)

    print(f"File downloaded successfully: {tarfile_path}")
    with tarfile.open(tarfile_path, "r") as tar:
        tar.extractall(path=cwd)
    print(f"File extracted successfully to '{cwd}'")
    os.remove(tarfile_path)
    print("Tar file deleted successfully.")

def switch_directory(cwd):
    for dir in os.listdir(os.path.join(cwd,'lfw')):
        for file in os.listdir(os.path.join(cwd,f'lfw\{dir}')):
            ex_path = os.path.join(f'{cwd}\lfw\{dir}',file)
            new_path = os.path.join(neg_path,file)
            os.replace(ex_path,new_path)
    # os.remove(os.path.join(cwd,'lfw'))

if __name__=="__main__":
    url = "http://vis-www.cs.umass.edu/lfw/lfw.tgz"
    download_data(url,cwd)
    switch_directory(cwd)