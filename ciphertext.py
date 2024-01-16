class Cipher:
    def __init__(self):
        self.cipher_list = []
        self.cipher_str = ""
        self.cipher_num = 0
        print("암호화 및 복호화 프로그램이 활성화 되었습니다.")
    def encryption(self, input_str, num):
        print("암호화 시작")
        for i in input_str:
            if i == " ":
                self.cipher_list.append(i)
            else:
                self.cipher_list.append(chr(ord(i) + num))
        input_str = "".join(self.cipher_list)
        self.cipher_str = input_str
        self.cipher_num = num
        return input_str

    def decryption(self):
        print("복호화 시작")
        if len(self.cipher_list) > 0:
            self.cipher_list = []
        for i in self.cipher_str:
            if i == " ":
                self.cipher_list.append(i)
            else:
                self.cipher_list.append(chr(ord(i) - self.cipher_num))
        str = "".join(self.cipher_list)
        return str
