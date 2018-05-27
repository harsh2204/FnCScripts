##File Transfer Script
---

<sub>PS: I personally don't consider this one a script but it is simple and useful, so it is here.</sub>

This script allows you to transfer a file over the http download protocol with the help of a python simple http server. Follow the steps to setup the server. This will become very easy once you have completed the entire process atleast once:

  + Copy the desired file into the folder of this 'script'.
  + Copy the file name including the extension. (A shortcut is F2 -> Ctrl+A -> Ctrl+C)
  + Open the index.html file in a text editor and replace the 'filename.ext' with the file name you've copied.
  + Finally, depending on the version of python you have use on of the following:
    * Python 2.7
      ```
      $python -m SimpleHTTPServer 8080
      ```
      * Python 3.x
        ```
        $python -m http.server 8080
        ```
  + You are now server the file over your network. This file can be accessed by other devices on your network by using the IP Address of your serving device. The IP Address can be obtained by using the `ipconfig` command and getting the "IPv4 Address". For example an internal IP Address looks like "192.168.0.31".
  + You can finally access your file on the desired device just by typing in this address and putting a `:8080` after the address. So finally your address should look like "192.168.0.31:8080"
---

###Disclaimer
This is not a secure way to transfer files over a network as anyone on the network has access to them while the server is up and running. If secure file transfer is something you are looking for, then look into finished products like Push Bullet.
