# SimpleTextLockbox
GUI application that password protects the contents of files. The program either reads the contents of an existing file or creates a new file from user input, then encrypts those contents using AES. A unique key is generated from a user inputted password, which can be used to both encrypt and decrypt file contents to hide or reveal information. 

# Basic Usage
To open a file, simply click on the open button
![1](https://user-images.githubusercontent.com/97146562/148957002-5f8c0e55-9170-4d28-b992-82041dbf6daa.png)

A file dialog window will open up. Navigate to the location of the file that you wish to encrypt and open it.
![2](https://user-images.githubusercontent.com/97146562/148958024-5c34e9a1-fbae-491c-b5a2-1f39d4f44447.png)

The contents of that file will appear in the textbox. 
![3](https://user-images.githubusercontent.com/97146562/148957411-c5059150-9520-49f5-811f-c6d0b688eacb.png)

After clicking on the encrypt button, a password prompt will appear. The password to be entered will be used to both encrypt and decrypt file contents.

![4](https://user-images.githubusercontent.com/97146562/148958172-5173c4a0-0ab3-4f76-abd8-24baa46f5c3f.png)

The file contents will now be encrypted and the original information will be hidden.
![5](https://user-images.githubusercontent.com/97146562/148958612-2d282f47-7f79-4a0d-8605-4d25de107665.png)

After clicking on the decrypt button, a password prompt will appear again. This password must be the same as the password that was used to encrypt the file contents.
![7](https://user-images.githubusercontent.com/97146562/148958902-387043c0-6112-4baf-b85b-8b3650b07429.png)

The decrypted contents will be displayed in the textbox.
![8](https://user-images.githubusercontent.com/97146562/148959420-041ab30d-ac3d-4e66-8a55-c7994f1b1aa6.png)
