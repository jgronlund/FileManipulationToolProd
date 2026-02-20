This is a lightweight command line interface utility meant for file manipulation tasks including:

1) Create a file

2) Copy file to a destination

3) Combine 2 files into a third file 

4) Delete a file

-----------------------------------------------------------------------------------

System Requirements:
Debian or Ubuntu-based Linux System
Python 3.9+

-----------------------------------------------------------------------------------

Instructions on installing filetool:
1) Download filetool-deb.zip and install_filetool.sh onto your linux computer

2) Now Install the debian

    Open up the Terminal and change directories to be in the same directory as the files you just downloaded and run the following commands:

    Unzip filetool-deb.zip
    - unzip filetool-deb.zip
    
    Installing the debian
    Option 1 - Install from .deb
        - sudo dpkg -i filetool_0.1.0-1_all.deb
        - sudo apt -f install -y
    
    Option 2 - Install using the provided Bash Script (this would be useful for bigger projects)
        Make the install file executable
        - chmod +x install_filetool.sh

        Run the installer adding in the correct filepath to the .deb file
        - ./install_filetool.sh filetool_0.1.0-1_all.deb

3) Now the filetool should be installed. To test, type in the terminal:
    - filetool --help
    You should see a help menu pop-up with instructions on how to use the application

-----------------------------------------------------------------------------------

For Instructions on using the filetool application please use the --help option. Below are brief instructions:
1) Show Help
    - filetool --help

2) Create a File with content
    - filetool create example.txt --content "Hello World"

3) Copy a File
    - filetool copy source.txt destination.txt

4) Combine Two Files
    - filetool combine a.txt b.txt combined.txt

5) Delete a File
    - filetool delete file.txt

-----------------------------------------------------------------------------------

Testing:
    This project includes both unit and integration tests using pytest.

    To run tests please see DEVELOPER.md

    

