from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.clipboard import Clipboard
############################################# Cryptography and Hashing
from cryptography.fernet import Fernet
import bcrypt
import random


errors = 0

KeyTextXXX = []

# call the function, passing the file and line to skip

class MainWindow(Screen):
    pass
class SecondWindow(Screen): # This is the window for encrypting

    def encrypteddata(self, *args): # Encrypting data
        global KeyTextXXX
        try:
            if self.plaintext.text == '': # If the plain text is empty
                self.submited.text = 'Need message to encrypt!'
                self.key.text = str('No key generated')
                self.encrypt.text = 'Encryption failed'
            else:
                plaintextdata = self.plaintext.text

        ##########################################Key
                key = Fernet.generate_key()
                KeyTextXXX.append(key.decode('utf-8'))
                self.key.text = str('Secret Key Generated')

        ##########################################Key/Encrypt


                crypter = Fernet(key) # object
                encryptedOne = crypter.encrypt(bytes(plaintextdata, 'utf-8'))
                self.encrypt.text = str(encryptedOne)
                KeyTextXXX.append(encryptedOne.decode('utf-8'))
        ##########################################encrypt

                self.submited.text = 'Encrypted with success!'
        except:
            self.submited.text = 'Error!'
    def copytoclipboard(self,*args):
        try:
            #Randomize the password

                global KeyTextXXX
                text_random = 'aAbBcCdDeEfFgGhHiI1234jJm56789MnNkKlLoO$432^12&^%&^*((__"?!@##$%^&*()_+{}:">?<;'
                xlm = random.choice(text_random)
                xlm2 = random.choice(text_random)
                xlm3 = random.choice(text_random)
                xlm4 = random.choice(text_random)

                Encrypted_data = KeyTextXXX[1]
                Key_data = KeyTextXXX[0]
                indexsupply1 = []

            #Make the password stronger

                for index in Key_data:
                    indexsupply1.append(index)
                indexsupply1.insert(8, xlm)
                indexsupply1.insert(13, xlm3)
                indexsupply1.insert(37, xlm2)
                indexsupply1.insert(30, xlm3)
                indexsupply1.insert(25, xlm4)
                finalstageKey = str('')

                for index in indexsupply1:
                    finalstageKey += str(index)
                Clipboard.copy(Encrypted_data + '\n' + f'{xlm4}{finalstageKey}{xlm}{xlm2}{xlm3}')
                self.encrypt.text = 'Encrypted data'
                self.key.text = 'Key'
                self.plaintext.text = ''
                KeyTextXXX.clear()

        except:
            pass
    def pastetoclipboard(self,*args): # Copy to clipboard
        self.plaintext.text = Clipboard.paste()



class ThirdWindow(Screen): # This is the window for decrypting

    def dencrypteddata(self, *args): # Decrypting data
        try:
            plaintextdata = self.plaintext.text
            encrypteddata = self.encrypt.text
            splitencrypteddata = encrypteddata.split()
            spltenc = splitencrypteddata[1]
            encrkeyx = str(spltenc)
            listedindex = []

            # Decrypting the additional function

            for index in encrkeyx:
                addindextolist = listedindex.append(index)
            listedindex.pop(0)
            listedindex.pop(8)
            listedindex.pop(12)
            listedindex.pop(23)
            listedindex.pop(28)
            listedindex.pop(35)
            listedindex.pop(44)
            listedindex.pop(44)
            listedindex.pop(44)

            finalstageKey = str('')
            for index in listedindex:
                finalstageKey += str(index)



            FinalKeyX = finalstageKey
            FinalEncryptedData = splitencrypteddata[0]

            coded1 = FinalEncryptedData.encode('utf-8')
            coded2 = FinalKeyX.encode('utf-8')

            crypter = Fernet(coded2)

            decryptedOne = crypter.decrypt(coded1)

            self.submited.text = 'Decrypted with success!'
            self.plaintext.text = decryptedOne.decode('utf-8')
            self.encrypt.text = ''
        except:
            self.submited.text = 'Need encrypted data and key to decrypt!'
            self.plaintext.text = 'Need encryption data'
            # print(coded2)

    def copytoclipboard(self,*args): # Copy to Clipboard Decrypted data
        try:
            if self.plaintext.text == 'Decrypted text here':
                pass
            else:
                Clipboard.copy(self.plaintext.text)
                self.plaintext.text = 'Decrypted text here'
        except:
            pass

    def pastetoclipboard(self,*args): # Paste Clipboard
        self.encrypt.text = Clipboard.paste()



class ForWindow(Screen): # Greetings Window and security
    def on_pre_enter(self, *args):
        self.welcome.text = str((f'Greetings!')) # pre enter on enter pre leave !

    def passwordkeep(self, *args): # Password verification and Hashing
        global errors
        try:
            if bcrypt.checkpw(bytes(self.passwordS.text,'utf-8'), b'$2b$14$T1U44OjL0anYq4MCj1P.bOJKs961Ckfsou1DO4ru.ksswGRLIFz/y'): # Password + salt
                self.manager.current = 'third'
                self.passwordS.text = ''
            else:
                errors += 1
                self.welcome.text = 'Security Errors---> ' + f'{errors}/3'
        except:
            pass

        if errors == 4: # If the password is entered incorrectly it exits the application
            App.get_running_app().stop()


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('style.kv')

class EncryptXF2(App):
    def build(self):
        self.icon = 'icon.png'
        global Account
        return kv


EncryptXF2().run()

