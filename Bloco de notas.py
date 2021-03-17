import datetime
import sqlite3


#Hora, minuto, segundo, e data
date = datetime.datetime.now()

#Looping
while True:
    
    
    opções = int(input('\nQual operação deseja fazer? (1) Escrever uma anotação, (2) Ver todas anotações, (3)Apagar uma anotação, (4)Editar uma anotação , (5)Apagar todas as anotações, \n(6) Ver uma anotação por Id, (7)Sair: '))


    
    #Cria uma conexão 
    conn = sqlite3.connect('Anotações.db')
    
    #Cria um cursor
    c = conn.cursor()

    #Criando uma tabela
    c.execute('CREATE TABLE IF NOT EXISTS Anotações(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Data TEXT,Título VARCHAR(30) ,\
            Anotação VARCHAR(500))')
            

    #Opção (1) Escrever uma anotação
    if opções == 1:
            
        titulo = input('Escreva um título:\n')
        anotação = input('Escreva sua anotação:\n')

        #Inserindo dados
        c.execute('INSERT INTO Anotações (Data, Anotação, Título) VALUES (?,?, ?)', (date, anotação, titulo))
        conn.commit()
        print('Anotação salvada com sucesso!')


    #Opção (2) Ver todas anotações
    elif opções == 2:
        c.execute('SELECT * FROM Anotações')
        print('\n(ID, Data, Título, Anotação)')
        for line in c.fetchall():
            print(line, '\n')


    #Opção (3)Apagar uma anotação
    if opções == 3:
        a = input('Digite o ID da sua anotação  que deseja excluir: ')
        perg = int(input('Gostaria mesmo de excluir? Se sim digite 1 se não digite 2: '))
        if perg == 1:
            c.execute('DELETE FROM Anotações WHERE Id == (?) ', (a))
            conn.commit()
            print('\nExcluído com sucesso!')
            

    
    #Opção (4)Editar uma anotação
    elif opções == 4:
        b = input('Digite o ID da anotação que deseja editar: ')
        anotação = input('Escreva sua nova anotação:\n')
        c.execute('UPDATE Anotações SET Anotação == (?) WHERE Id == (?)', (anotação, b))
        conn.commit()
        print('\nEditado com sucesso!')


    
    #Opção (5)Apagar todas as anotações
    elif opções == 5:
        perg = int(input('Gostaria mesmo de excluir? Se sim digite 1 se não digite 2: '))
        if perg == 1:   
            c.execute('DELETE FROM Anotações ')
            conn.commit()
            print('\nExcluído com sucesso!')


    
    #Opção (6) Ver uma anotação por Id
    elif opções == 6:
        d = input('Digite o ID da anotação que deseja ver: ')
        c.execute('SELECT Anotação FROM Anotações WHERE id ==(?)', (d))
        for line in c.fetchall():
            print(line)

    
    
    #Finaliza o looping
    elif opções == 7:
        break 


#Fechando a conexão e o cursor
c.close()
conn.close()