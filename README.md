# HTB-Snoopy LFI Exploit  
  
This script exploits a Local File Inclusion (LFI) vulnerability in the `download.php` file of the HackTheBox machine Snoopy (HTB-Snoopy). It retrieves and displays the content of files on the machine using this vulnerability.  
  
## Workflow  
  
1. Receive user input for a file path.  
2. Encode the path to bypass the server-side restrictions.  
3. Construct the URL to exploit the LFI vulnerability.  
4. Check if the file exists by sending a HEAD request.  
5. If the file exists, download it as a ZIP file.  
6. Extract the ZIP file and display the content of the extracted file.  
  
## Functions  
  
### download_file(url: str, filename: str) -> str  
  
This function downloads a file from the specified URL and saves it with the provided filename.  
  
**Arguments:**  
  
- `url` (str): The URL of the file to download.  
- `filename` (str): The filename to save the downloaded file as.  
  
**Returns:**  
  
- `str`: The saved filename.  
  
### extract_zip(zip_path: str, extract_path: str) -> None  
  
This function extracts the contents of a ZIP file to the specified extraction path.  
  
**Arguments:**  
  
- `zip_path` (str): The path of the ZIP file to extract.  
- `extract_path` (str): The path to extract the contents of the ZIP file to.  
  
### print_file_content(file_path: str) -> None  
  
This function prints the content of the specified file with magenta-colored text.  
  
**Arguments:**  
  
- `file_path` (str): The path of the file to read and print its content.  
