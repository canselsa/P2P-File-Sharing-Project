# P2P-File-Sharing-Project

The Project is Python Based Peer to Peer (P2P) File Sharing System. The Purpose of this Project is to exchange files between two remote hosts.


- Features of Project 
There are several features of P2P File Sharing system:

```
This Project have 4 processes:
1. Service Listener 
2. Service Announcer 
3. P2P Downloader 
4. P2P Server.
```

- **We merged all 4 processes in two files – Client and Server.**

But these processes should work as outlined in their respective specifications. 
1. Successfully detect all available users in the Local Area Network. 
2. Successfully exchange files with any available user in the Local Area Network. 
3. Display an error dialog if a download is in error. 
4. Output a download log, containing timestamps and names of all downloaded files

Server.py discovers all online users. The content reference can keep up to 10 users’ contents, with each having up to 10 chunks, with each chunk carried by at most all other users. P2P Downloader downloads a file from any online user, with no perceivable delay. Any unspecified configuration is a plus – displaying download progress, displaying an error message when file chunks can’t be downloaded from peers.

Once the file is ready, the P2P Downloader informs the user through the terminal that the file has been successfully downloaded. Downloaded files can be found on Desktop (or Download file). P2P Server.py served filenames in a Server log (a text file - log.txt) under the same list. Each entry specifies timestamp, sent to IP address, sent chunk name. Later a TCP session is closed, P2P Server and P2P Downloader continue; the service will not stop.


```
# How to Run
1. Setup Server
Run "server.py" directly. "Ctrl + C" to shutting down the server.

2. "client.py" 
On the Kali's Terminal, user should execute program as root(Administrator).
After running the code, you will Enter the Client Ip. 
Program will display "Filename" - If the file exists you are going to see "File exists".

You can enter "Y" or "N"
Y - Yes
N - No


If you want to download the file "Press Enter for file download". 
When the downloading ends you can find the Downloaded file in your Documents.
```
