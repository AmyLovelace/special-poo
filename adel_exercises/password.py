from human import Human

def password_generator():

    # SE GENERA UNA INSTANCIA QUE SE GUARDA EN LA VARIABLE user1
    user1 = Human('Amy', 18)
    user1.set_password(10)


    user2 = Human('Inay', 8)
    user2.set_password(20)

    user3 = Human()

    print(user1.password)
    print(user2.password)
    print(user1.name)
    #print(user1.__age)
    print(user2.name)
    #print(user2.__age)
    print(user2.soul)
    print(user3.soul)

    user3.status(False)
    print(user1.soul)
    print(user2.soul)
    print(user3.soul)
    print(user2.get_age())
    print(user2.kingdom)
    print(user2.type)


password_generator()

# clase = objeto => molde para clonar infinitas veces el objectos en instancias
