# Password Locker
#### By Oyesa Mercy Oluchina
#### 22/04/2022

### Description
Password Locker is a python application that manages the user’s passwords as well as generate unique passwords for the user.  

### Screenshot
### Behaviour Driven Development (BDD)

| Behaviour                            |     Input                       |                                                                                                       Output |
| :---                                 |     :---:                       |                                                                                                         ---: |
|Open the application on the terminal  |       Run command $ ./main.py   |                         Hello Welcome Password Locker.* CNA --- Create New Account * LI --- Have An Account  |
|Select CNA                            |   input username and password   |                       Hello username, Your account has been created succesfully! Your password is: password  |
|Select LI                             |Enter your username and password |                                                         Shortcode menu to help you navigate the application  |
|Save details in the application       |   Enter                         |Enter account, username, password and choose IP to input password or GRP for the app to generate your password|
|Display stored details                |   Enter DD                      |                                  Here's your list of saved accounts or You don't have any saved details yet  |
|Find stored details using account name|   Enter FD                      |                                                              Enter the Account Name you want to search for   |
|Delete existing account detail        |   Enter D                       |                                                     Enter the account name whose details you want to delete  |
|Exit Application                      |   Enter EX                      |                                                              User exits application                          |


### Setup/Installation Requirements
The application requires the following installations to operate:
  -Python3.8
  -Pyperclip
  -Pip

With the above installations proceed to:
 -git clone https://github.com/oyesa/Password-Locker.git
 -cd password-locker
 -code . (if using Visual Studio Code) 

 ### Running Application
 To run password locker, open the cloned files in your terminal and run the following commands:
  $ chmod +x main.py
  $ ./main.py

 ### Technologies Used
-Python3.8


### Bugs
No known bugs
In case you run into any bug/problem feel free to contact me

## Contact
Oyesa Oluchina -mercy.oluchina@student.moringaschool.com

 ### Licence
 MIT Licence
 Copyright (c) 2022 Oyesa Mercy Oluchina