import requests

def download_pcap_file(url, local_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(local_path, 'wb') as pcap_file:
            pcap_file.write(response.content)

        print(f"Downloaded the .pcap file to {local_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading the file: {e}")

if __name__ == "__main__":
    # Replace 'your_url' with the actual URL of the .pcap file you want to download
    pcap_url = 'https://github.com/broyogesh88/ocassignments/raw/main/pcap_file.pcap'

    # Replace 'local_directory' and 'file_name.pcap' with your desired local directory and file name
    local_directory = 'C:/Users/Lenovo/Desktop/'
    local_file_name = 'sample_traffic.pcap'
    local_path = local_directory + local_file_name

    download_pcap_file(pcap_url, local_path)
