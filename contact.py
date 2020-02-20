class Contact:
    def __init__(self,name,phone_number,e_mail,addr):
        self.name=name
        self.phone_number=phone_number
        self.e_mail=e_mail
        self.addr=addr

    def print_info(self):
        print("Name:",self.name)
        print("Phone Number:", self.phone_number)
        print("E-mail:", self.e_mail)
        print("Address:", self.addr)

def print_menu():
    print("1.연락처 입력")
    print("2.연락처 출력")
    print("3.연락처 삭제")
    print("4.종료 기능")
    menu =input("1~4까지의 번호를 입력해주세요")
    return int(menu)
def print_contact(contact_list):
    for contact in contact_list:
        contact.print_info()

def delete_contact(contact_list,name):
    for i, contact in enumerate(contact_list):
        if contact.name == name:
            del contact_list[i]

def set_contact():
    name=input("이름을 입력하세요")

    phone_number=input("전화번호를 입력하세요")

    e_mail=input("이메일을 입력하세요")

    addr=input("주소를 입력하세요")

    contact = Contact(name,phone_number,e_mail,addr)
    return contact

def run():
    contact_list = []
    while 1:
        menu = print_menu()
        if menu == 1:
            contact =set_contact()
            contact_list.append(contact)

        elif menu == 2:
            print_contact(contact_list)

        elif menu == 3:
            name = input("Name: ")

        elif menu==4:
            break
if __name__=="__main__":
    run()