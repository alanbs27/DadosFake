from faker import Faker
import pandas as pd

fake = Faker('pt_BR')

#O código abaixo criara 10 nomes diferentes
# fake.name()
# for _ in range(10):
#     print(fake.name())
#Gerando dados
fake.name()
fake.text()
fake.address()
fake.email()
fake.date()
fake.country()
fake.phone_number()
fake.random_number(digits=8)

#Criando o dataframe
fakeDataFrame = pd.DataFrame({'date': [fake.date() for i in range(5)],
                              'name': [fake.name() for i in range(5)],
                              'email': [fake.email() for i in range(5)],
                              'address': [fake.address() for i in range(5)],
                              'phone_number': [fake.phone_number() for i in range(5)],
                              'number': [fake.random_number(digits=8) for i in range(5)],
                              'country': [fake.country() for i in range(5)]})

print(fakeDataFrame)


