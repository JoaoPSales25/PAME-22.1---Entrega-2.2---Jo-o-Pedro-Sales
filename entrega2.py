

class sala:

    def __init__(self, nome, capacidade, abertura, fechamento):
        self.nome = nome #str nome/numero da sala
        self.capacidade = capacidade #int da capacidade maxima da sala
        self.abertura = abertura #int da hora de abertura
        self.fechamento = fechamento #int da hr de fechamento
        self.disciplinas = [] #list de strings disciplinas lecionadas nessa sala
        self.dias = [] #list de list (5) contendo outra list dos horarios(24) disponiveis ou nao de acordo com o dia (seg a sexta) sendo seg = [0],..sexta = [4]
        for i in range(5):
            self.dias.append([])
        for i in range(5):
            for j in range(24):
                self.dias[i].append("")

class professor:

    def __init__(self, nome):
        self.nome = nome #string nome do professor
        self.disciplinas = [] #list de str das disciplinas que ele está associado
        self.dias = [] #list de list (5) contendo outra list dos horarios das disciplinas dia (seg a sexta) sendo seg = [0],..sexta = [4]
        for i in range(5):
            self.dias.append([])
        for i in range(5):
            for j in range(24):
                self.dias[i].append("")

class aluno :

    def __init__(self, nome):
        self.nome = nome #string nome do aluno
        self.disciplinas = [] #list de str das disciplinas que aluno está cursando
        self.dias = [] #list de list (5) contendo outra list dos horarios das disciplinas dia (seg a sexta) sendo seg = [0],..sexta = [4]
        for i in range(5):
            self.dias.append([])
        for i in range(5):
            for j in range(24):
                self.dias[i].append("")

class disciplina:

    def __init__(self, nome, dias, hora, duracao, max):
        self.nome = nome #str nome da disciplina
        self.hora = hora #int hora que começa a disciplina
        self.dias = dias #list de ints contendo os numeros dos dias da disciplina (sendo seg = 0 .. sex = 4 )
        self.duracao = duracao #int contendo a duração da aula em horas
        self.max = max #int do numero maximo de alunos na sala
        self.alunos = [] #lista de str dos alunos inscritos
        self.professor = [] #lista unica com o professor da disciplina
        self.sala = [] #lista unica com a sala da disciplina

class interface: # interface do sistema

    def __init__(self):
        self.disciplinas = {} #dic de {nome da disciplina : disciplina} 
        self.salas = {} #dic {nome da sala : sala}
        self.professores ={} #dic {nome da professor : professors}
        self.alunos = {} #dic {nome da aluno : aluno}

    def start(self): #função que chama as outras (início)
        print("") #pular linha
        acao = input ("Digite a ação quer realizar (criar, listar, mostrar, associar, desassociar, excluir, alterar): ")
                              #vê o que ele quer criar e chama a função correspondente
        if acao == 'criar' or acao == "c":
            self.criar()
        elif acao == 'listar' or acao == "l":
            self.listar()
        
        elif acao == 'mostrar' or acao == "m":
            self.mostrar()

        elif acao == 'associar' or acao == "as":
            self.associar()

        elif acao == 'desassociar' or acao == "d":
            self.desassociar()

        elif acao == 'excluir' or acao == "e":
            self.excluir()
        
        elif acao == 'alterar' or acao == "al":
            self.alterar()
        else: 
            return self.start()


    #funcoes básicas (criar, excluir, alterar, mostrar, listar, associar, desasociar)

    def criar (self) :
        #cria uma sala de aula, um professor, um aluno ou uma disciplina
        print("")  #pular linha
        objeto = input ("Digite o que quer criar (sala, professor, aluno ou disciplina): ")
                              #vê o que ele quer criar e chama a função correspondente

        if objeto == 'sala' or objeto == 's':
            print("")  #pular linha
            
            nome = '' #input
            while (not nome.strip().isdigit()) or int(nome) < 0 or int(nome) > 200: #repete a pergunta até que seja um numero entre 0 e 200(numero max escolhido arbitrariamente
                nome = input("Insira um número para a sua sala (Entre 0 e 200): ") #str com um numero

            capacidade = ""
            while (not capacidade.strip().isdigit()): #checa se é um digito e se é maior que zero
                capacidade = input("Insira o número máximo de alunos na sala: ")

            abertura = ""
            while (not abertura.strip().isdigit()): #checa se é um digito e se é maior que zero
                abertura = input("Insira a hora de abertura: ")

            fechamento = ""
            while (not fechamento.strip().isdigit()): #checa se é um digito e se é maior que zero
                fechamento = input("Insira a hora de fechamento: ")

            self.criar_sala(nome, capacidade, abertura, fechamento)

        elif objeto == 'professor' or objeto == 'p':
            print("")  #pular linha
            n = input("Nome do professor: ")
            self.criar_professor(n)

        elif objeto == 'aluno' or objeto == 'a':
            print("")  #pular linha
            n = input("Nome do aluno: ")
            self.criar_aluno(n)

        elif objeto == 'disciplina' or objeto == 'd':
            print("")  #pular linha
            n = input("Nome da disciplina: ") #pergunta o nome da disciplina
        
            hora = "" #input
            while (not hora.strip().isdigit()) or int(hora) > 23: #checa se é um digito e se é menor ou igual que 23
                print("")  #pular linha
                hora = input("Horario de inicio da disciplina (h): ")
            

            dias = []; #list de str que quarda os dias (seg= '0', .. sex= '4')
            dia = "" #input
            while '5' not in dias: #5 significa que finalizou de inserir os dias
                while (not dia.strip().isdigit()) or int(dia) > 5: #repete se não se enquadrar
                    print("")  #pular linha
                    dia = input("Adicione um dia de aula (0 - seg/ 1 - ter/ 2 - qua /3 - quinta / 4 - sexta/ 5 - finalizar): ")
                if dia not in dias: #adiciona o dia na lista de dias
                        dias += dia   
                dia = ""
                print("")  #pular linha

            dias.remove('5') #remove o 5 da lista (finalizar operação)
            for i in range(0, len(dias)): #converte em uma lista de inteiros
                dias[i] = int(dias[i])

            duracao = '' #input
            while (not duracao.strip().isdigit()) or int(duracao) + int(hora) > 23: #checa se é um digito e se é menor que 4 (escolhi arbitrariamente) e repete a pergunta
                duracao = input("Duração da disciplina (em horas): ")
            print("")  #pular linha
            
            max = '' #input
            while (not max.strip().isdigit()): #checa se é um digito e repete a pergunta
                max = input("Máximo de alunos: ")
            print("")  #pular linha

            self.criar_disciplina(n, dias, hora, duracao, max)

        else:                           #se digitou outra coisa repete a pergunta
            return self.criar()

        return self.start() #volta pro inicio

    def listar (self):
        print("") #pular linha
        acao = input ("Digite o que deseja listar (salas, professores, alunos ou disciplinas): ")

        if acao == "salas" or acao == "s": #checa qual acao deve tomar
            print("")  #pular linha
            self.listar_salas()
        elif acao =="professores" or acao == "p":
            print("")  #pular linha
            self.listar_professores()
        elif acao =="alunos" or acao == "a":
            print("")  #pular linha
            self.listar_alunos()
        elif acao =="disciplinas" or acao == "d":
            print("")  #pular linha
            self.listar_disciplinas()
        else:                            #se digitou outra coisa repete a pergunta
            return self.listar()

        return self.start() #volta pro inicio
    
    def mostrar (self):
        print("") #pular linha
        acao = input ("Digite o que deseja mostrar (sala, professor, aluno ou disciplina): ")

        if acao == "sala" or acao == "s": 
            print("")  #pular linha
            s = input("Digite o numero da sala: ")
            self.mostrar_sala(s)

        elif acao =="professor" or acao == "p":
            print("")  #pular linha
            p = input("Digite o nome do professor: ")
            self.mostrar_professor(p)
    
                
        elif acao =="aluno" or acao == "a":
            print("")  #pular linha
            a = input("Digite o nome do aluno: ")
            self.mostrar_aluno(a)
          

        elif acao =="disciplina" or acao == "d":
            print("")  #pular linha
            d = input("Digite o nome da disciplina: ")
            self.mostrar_disciplina(d)

        else:                            #se digitou outra coisa repete a pergunta
            return self.mostrar()

        return self.start() #volta pro inicio

    def associar(self):
        print("") #pular linha

        acao = input ("Digite o que deseja associar (sala, professor, aluno): ")
        print("") #pular linha

        dis = input ("Digite qual disciplina deseja que seja associada: ")

        if acao == "sala" or acao == "s": 
            print("")  #pular linha
            s = input("Digite o numero da sala: ")
            self.associar_sala(s, dis)

        elif acao =="professor" or acao == "p":
            print("")  #pular linha
            p = input("Digite o nome do professor: ")
            self.associar_professor(p, dis)
    
                
        elif acao =="aluno" or acao == "a":
            print("")  #pular linha
            a = input("Digite o nome do aluno: ")
            self.associar_aluno(a, dis)
          
        else:                            #se digitou outra coisa repete a pergunta
            return self.associar()

        return self.start() #volta pro inicio

    def desassociar(self):
        print("") #pular linha
        acao = input ("Digite o que deseja desassociar (sala, professor, aluno): ")
        dis = input ("Digite qual disciplina deseja que seja desassociada: ")

        if acao == "sala" or acao == "s": 
            print("")  #pular linha
            s = input("Digite o numero da sala: ")
            self.desassociar_sala(s, dis)

        elif acao =="professor" or acao == "p":
            print("")  #pular linha
            p = input("Digite o nome do professor: ")
            self.desassociar_professor(p, dis)
                
        elif acao =="aluno" or acao == "a":
            print("")  #pular linha
            a = input("Digite o nome do aluno: ")
            self.desassociar_aluno(a, dis)
          
        else:                            #se digitou outra coisa repete a pergunta
            return self.desassociar()

        return self.start() #volta pro inicio

    def excluir (self): 
        print("") #pular linha

        acao = input ("Digite o que deseja excluir (sala, professor, aluno, disciplina): ")

        if acao == "sala" or acao == "s": 
            print("")  #pular linha
            s = input("Digite o numero da sala: ")
            self.excluir_sala(s)

        elif acao =="professor" or acao == "p":
            print("")  #pular linha
            p = input("Digite o nome do professor: ")
            self.excluir_professor(p)
                
        elif acao =="aluno" or acao == "a":
            print("")  #pular linha
            a = input("Digite o nome do aluno: ")
            self.excluir_aluno(a)

        elif acao =="disciplina" or acao == "d":
            print("")  #pular linha
            d = input("Digite o nome da disciplina: ")
            self.excluir_disciplina(d)
          
        else:                            #se digitou outra coisa repete a pergunta
            return self.desassociar()

        return self.start() #volta pro inicio

    def alterar (self):
        #altera uma sala de aula, um professor, um aluno ou uma disciplina
        print("")  #pular linha

        objeto = input ("Digite o que quer alterar (sala, professor, aluno ou disciplina): ")
        #vê o que ele quer criar e chama a função correspondente

        if objeto == 'sala' or objeto == 's':
            print("")  #pular linha
            o = input("Insira a sala a ser alterada: ")

            nome = '' #input
            while (not nome.strip().isdigit()) or int(nome) < 0 or int(nome) > 200: #repete a pergunta até que seja um numero entre 0 e 200(numero max escolhido arbitrariamente
                nome = input("Insira um novo número para a sua sala (Entre 0 e 200): ") #str com um numero

            capacidade = ""
            while (not capacidade.strip().isdigit()): #checa se é um digito e se é maior que zero
                capacidade = input("Insira o novo número máximo de alunos na sala: ")

            abertura = ""
            while (not abertura.strip().isdigit()): #checa se é um digito e se é maior que zero
                abertura = input("Insira a nova hora de abertura: ")

            fechamento = ""
            while (not fechamento.strip().isdigit()): #checa se é um digito e se é maior que zero
                fechamento = input("Insira a nova hora de fechamento: ")

            self.alterar_sala(o, nome, capacidade, abertura, fechamento)

        elif objeto == 'professor' or objeto == 'p':
            print("")  #pular linha
            o = input("Insira o professor a ser alteradd: ")
            n = input("novo nome do professor: ")
            self.alterar_professor(o, n)

        elif objeto == 'aluno' or objeto == 'a':
            print("")  #pular linha
            o = input("Insira o aluno a ser alteradd: ")
            n = input("novo nome do aluno: ")
            self.alterar_aluno(o, n)

        elif objeto == 'disciplina' or objeto == 'd':
            print("")  #pular linha

            o = input("Insira a disciplina a ser alterada: ")
            print("")  #pular linha

            n = input("novo nome da disciplina: ") #pergunta o nome da disciplina
        
            hora = "" #input
            while (not hora.strip().isdigit()) or int(hora) > 23: #checa se é um digito e se é menor ou igual que 23
                print("")  #pular linha
                hora = input("novo horario de inicio da disciplina (h): ")
            

            dias = []; #list de str que quarda os dias (seg= '0', .. sex= '4')
            dia = "" #input
            while '5' not in dias: #5 significa que finalizou de inserir os dias
                while (not dia.strip().isdigit()) or int(dia) > 5: #repete se não se enquadrar
                    print("")  #pular linha
                    dia = input("Novos dias de aula (0 - seg/ 1 - ter/ 2 - qua /3 - quinta / 4 - sexta/ 5 - finalizar): ")
                if dia not in dias: #adiciona o dia na lista de dias
                        dias += dia   
                dia = ""
                print("")  #pular linha

            dias.remove('5') #remove o 5 da lista (finalizar operação)
            for i in range(0, len(dias)): #converte em uma lista de inteiros
                dias[i] = int(dias[i])

            duracao = '' #input
            while (not duracao.strip().isdigit()) or int(duracao) + int(hora) > 23: #checa se é um digito e se é menor que 4 (escolhi arbitrariamente) e repete a pergunta
                duracao = input("Nova duração da disciplina (em horas): ")
            print("")  #pular linha
            
            max = '' #input
            while (not max.strip().isdigit()): #checa se é um digito e repete a pergunta
                max = input("Novo máximo de alunos: ")
            print("")  #pular linha

            self.alterar_disciplina(o, n, dias, hora, duracao, max)

        else:                           #se digitou outra coisa repete a pergunta
            return self.criar()

        return self.start() #volta pro inicio
    
    #funções criar

    def criar_sala (self, nome, capacidade, abertura, fechamento): #cria uma sala nova
        print("") #pular linha
        
        s = sala(nome, int(capacidade), int(abertura), int(fechamento)) #cria um obj da classe sala

        self.salas[s.nome] = s #salva a sala no dicionario das salas

        str = "Sala " + s.nome + " foi criada" #cria msg
        
        return print(str)

    def criar_disciplina(self, n, dias, hora, duracao, max): #cria disciplina com nome dias hora duração e maximo de alunos  
        print("") #pular linha

        d = disciplina(n, dias, int(hora), int(duracao), int(max))

        str = "Disciplina " + d.nome + " foi criada" #cria msg

        self.disciplinas[d.nome] = d #salva a disciplina no dicionario das disciplina
        
        return print(str) #printa a msg

    def criar_professor(self, n): #cria um professor sem nenhuma disciplina relacionada
        print("") #pular linha

        p = professor(n)
        str = "Professor " + p.nome + " foi adicionado"
        self.professores[p.nome] = p #salva professor no dicionario de professores
        return print(str)

    def criar_aluno(self,n): #cria um aluno sem nenhuma disciplina relacionada
        print("") #pular linha

        a = aluno(n)
        str = "Aluno " + a.nome + " foi adicionado"
        self.alunos[a.nome] = a #salva o professor no dicionario dos professores
        return print(str )


    #funções excluir

    def excluir_sala(self, sala):
        if sala in self.salas: #verifica se a sala existe
            self.salas.pop(sala) #tira ela do dicoinario
            return print("\n"+ "Sala " + sala + " foi removida")
        else:
            return print("\n" + "Sala não encontrada")

    def excluir_professor(self, professor):
        if professor in self.professores: #verifica se o prof existe
            self.professores.pop(professor)  #tira ele do dicoinario
            return print("\n"+ "Professor " + professor + " foi removido")
        else:
            return print("\n" + "Professor não encontrado")

    def excluir_aluno(self, aluno):
        if aluno in self.alunos: #verifica se o aluno existe
            self.alunos.pop(aluno) #tira ele do dicoinario
            return print("\n"+ "Aluno " + aluno + " foi removido")
        else:
            return print("\n" + "Aluno não encontrada")

    def excluir_disciplina(self, disciplina):
        if disciplina in self.disciplinas: #verifica se a disciplina existe
            self.disciplinas.pop(disciplina) #remove ela do dicionario
            return print("\n"+ "Disciplina " + disciplina + " foi removida")
        else:
            return print("\n" + "Disciplina não encontrada")


     #funções alterar (altera os parametros de quando foram criados os objetos)
    
    def alterar_sala(self, sala, nome_novo, capacidade_nova, abertura_nova, fechamento_novo): #altera capacidade da sala
        if sala in self.salas: #verifica se a sala existe
            aux = self.salas[sala].disciplinas.copy()
            self.excluir_sala(sala)
            self.criar_sala(nome_novo, capacidade_nova, abertura_nova, fechamento_novo) #faz as alterações
            print(aux)
            for d in aux: #desassocia e associa para caso a alteração faça com que requisitos deixem de ser cumpridos
                self.desassociar_sala(sala, d)
                self.associar_sala(nome_novo, d)

            return print('Alterações confirmadas')
        else:
            return print("\n" + "Sala não encontrada") 

    def alterar_professor(self, professor, nome_novo): #altera o nome do professor
        if professor in self.professores: #verifica se o prof existe
            self.excluir_professor( professor)
            self.criar_professor(nome_novo)
            return print('Alterações confirmadas')
        else:
            return print("\n" + "Professor não encontrado")

    def alterar_aluno(self, aluno, nome_novo): #altera o nome do aluno
        if aluno in self.alunos: #verifica se o aluno existe
            self.excluir_aluno(aluno)
            self.criar_aluno(nome_novo)
            return print('Alterações confirmadas')
        else:
            return print("\n" + "Aluno não encontrada")

    def alterar_disciplina(self, disciplina, nnome, ndias, nhora, nduracao, nmax): #altera nome, dias, horario, duração e max
        ###!!! se a alteração descumpriu algum prerequisito, a disciplina é desassociada
        if disciplina in self.disciplinas: #verifica se a disciplina existe

            self.excluir_disciplina(disciplina)
            self.criar_disciplina (nnome, ndias, int(nhora), int(nduracao), int(nmax))

            for a in self.alunos: #desassocia e associa os alunos associados a ela
                if nnome in self.alunos[a].disciplinas:                   
                    self.associar_aluno(a, nnome)

            for a in self.professores: #desassocia e associa os professores associados a ela
                if nnome in self.professores[a].disciplinas:
                    self.associar_aluno(a, nnome)

            for a in self.salas: #desassocia e associa salas associados a ela
                if nnome in self.salas[a].disciplinas:
                    self.associar_aluno(a, nnome)

            return print("\n"+ "alterações confirmadas")
        else:
            return print("\n" + "Disciplina não encontrada")



    #funções mostrar

    def mostrar_sala(self, nome):
        print("") #pular linha
        
        dias_da_semana = ['seg', 'ter', 'qua', 'qui', 'sex'] #list auxiliar
        if nome in self.salas:  #procura se a sala esta presente na lista das salas
            sala = self.salas[nome] #salva o objeto da classe de um certo nome na variavel sala
            string = '' 
            string += "Nome: " + sala.nome + "\n"
            string += "Dias: " + "\n"
            for i in range(5):
                string += dias_da_semana[i] + ": "
                for j in range(24):
                    string+= sala.dias[i][j] + " "
                string += "\n"
            string += "Capacidade: " + str(sala.capacidade) + "\n"
            string += "Abertura: " + str(sala.abertura) + "\n"
            string += "Fechamento: " + str(sala.fechamento) + "\n"
            string += "Disciplinas: " + str(sala.disciplinas) + "\n"

            return print(string)

        else: 
            return print("Sala não encontrada" + "\n") #caso nao esteja na lista
 
    def mostrar_professor(self, nome): #mostra o nome a a disciplina do professor
        print("") #pular linha

        dias_da_semana = ['seg', 'ter', 'qua', 'qui', 'sex'] #list auxiliar 
        if nome in self.professores:
            professor = self.professores[nome]
            string = ''
            string += "Nome: " + professor.nome + "\n"
            string += "Disciplinas lecionadas: "
            string += str(professor.disciplinas) + "\n"
            for i in range(5):
                string += dias_da_semana[i] + ": "
                for j in range(24):
                    string+= professor.dias[i][j] + " "
                string += "\n"
            return print(string)

        else: 
            return print("Professor não encontrado" + "\n") #caso nao esteja na lista

    def mostrar_aluno(self, nome): #mostra o nome e as disciplinas inscritas do aluno
        print("") #pular linha

        dias_da_semana = ['seg', 'ter', 'qua', 'qui', 'sex'] #list auxiliar 
        if nome in self.alunos:
            aluno = self.alunos[nome]
            string = ''
            string += "Nome: " + aluno.nome + "\n"
            for i in range(5):
                string += dias_da_semana[i] + ": "
                for j in range(24):
                    string+= aluno.dias[i][j] + " "
                string += "\n"
            return print(string)

        else: 
            return print("Aluno não encontrado" + "\n") #caso nao esteja na lista

    def mostrar_disciplina(self, nome): #mostra o nome, dias, hora, duracao, max da disciplina 
        print("") #pular linha

        if nome in self.disciplinas:
            disciplina = self.disciplinas[nome]
            string = ''
            string += "Nome: " + disciplina.nome + "\n"
            string += "Dias: " + str(disciplina.dias)  + "\n"
            string += "Horario de início: " + str(disciplina.hora) + "h" + "\n"
            string += "Duração: " + str(disciplina.duracao) + "h" + "\n"
            string += "Maximo de alunos: " + str(disciplina.max)  + "\n"
            return print(string)
        else:
            print ("Disciplina não encontrada" + "\n")


     #funções listar 

    def listar_salas(self): 
        print("") #pular linha
        str = 'Salas: '
        for chave in self.salas: #percorre as chaves na lista
            str+= chave + ", "
        print(str + "\n")
    
    def listar_professores(self):
        print("") #pular linha
        str = 'Professores: '
        for chave in self.professores:
            str+= chave + ", "
        print(str + "\n")
    
    def listar_alunos(self):
        print("") #pular linha
        str = 'Alunos: '
        for chave in self.alunos:
            str+= chave + ", "
        print(str + "\n")
    
    def listar_disciplinas(self):
        print("") #pular linha
        str = 'Disciplinas: '
        for chave in self.disciplinas:
            str+= chave + ", "
        print(str + "\n")


    #funções associar

    def associar_professor(self, nome, disciplina):
        print("") #pular linha

        if nome in self.professores: #checa se o professor ta cadastrado
            if disciplina in self.disciplinas: #chega se a disciplina esta cadastrada
                if self.disciplinas[disciplina].professor: #checa se a lista ta vazia, ou seja, se ja tem um prof associado
                    return print("Essa disciplina já possui um professor associado")
                p = self.professores[nome] #salva em p o obj professor
                d = self.disciplinas[disciplina] #salva em d o obj disciplina
                if disciplina not in p.disciplinas: #checa se a disciplina ja esta associada ou nao ao prof
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            if p.dias[j][i] != "": #se já tem algo nesse horario
                                return print("Horario não disponível")

                    p.disciplinas.append(disciplina)
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            p.dias[j][i] = str(i) + "h:" + d.nome + " "; #associa a disciplina no respectivo dia j e horario i

                    d.professor.append(nome) #adiciona o professor na lista de professor da disciplina  
                    return print(disciplina + " associada ao professor " + nome)
                else:
                    return print("disciplina já está associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("professor nao encontrado")
            
    def associar_aluno(self, nome, disciplina):
        print("") #pular linha

        if nome in self.alunos: #se o aluno esta cadastrado
            if disciplina in self.disciplinas: #se a disciplina esta cadastrada
                a = self.alunos[nome] #salva em a o obj aluno
                d = self.disciplinas[disciplina] #salva em d o obj disciplina
                if d.max <= len(d.alunos): #verifica se a disciplina ja esta cheia ou nap
                    return print("Disciplina já atingiu seu limite maximo de alunos")

                if disciplina not in a.disciplinas: #checa se a disciplina ja esta associada ou nao
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            if a.dias[j][i] != "": #se já tem algo nesse horario
                                return print("Horario não disponível")
                    
                    a.disciplinas.append(disciplina)
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            a.dias[j][i] = str(i) + "h:" + d.nome + " "; #associa a disciplina no respectivo dia j e horario i

                    d.alunos.append(nome)
                    return print(disciplina + " associada ao aluno " + nome)
                else:
                    return print("disciplina já está associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("aluno nao encontrado")

    def associar_sala(self, nome, disciplina):
        print("") #pular linha

        if nome in self.salas: #se o sala esta cadastrada
            if disciplina in self.disciplinas: #se a disciplina esta cadastrada
                s = self.salas[nome] #salva em a o obj s
                d = self.disciplinas[disciplina] #salva em d o obj disciplina

                if s.capacidade < d.max: 
                    return print("O numero máximo de alunos da disciplina excede a capacidade da sala")

                if d.sala: #checa se a lista ta vazia, ou seja, se ja tem uma sala associada
                    return print("Essa disciplina já possui uma sala associada")

                if disciplina not in s.disciplinas:
                    
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            if i < s.abertura or i>s.fechamento:
                                return print("Horario não bate com o horario de funcionamento da sala")
                            if s.dias[j][i] != "": #se algum horario nao esta disponivel
                                return print("Horario não disponível")

                    s.disciplinas.append(disciplina) #adiciona disciplina na lista
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            s.dias[j][i] = str(i) + "h: " + d.nome + " "; #associa a disciplina no respectivo dia j e horario i
                    
                    d.sala.append(nome) #adiciona a sala na lista de sala da disciplina  

                    return print(disciplina + " associada à sala " + nome)
                else: 
                    return print("disciplina já está associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("aluno nao encontrado")


     #funções desassociar

    def desassociar_professor(self, nome, disciplina):
        print("") #pular linha

        if nome in self.professores: #checa se o professor ta cadastrado
            if disciplina in self.disciplinas: #chega se a disciplina esta cadastrada
                p = self.professores[nome] #salva em p o obj professor
                d = self.disciplinas[disciplina] #salva em d o obj disciplina
                if disciplina in p.disciplinas: #checa se a disciplina ja esta associada ou nao
                    p.disciplinas.remove(disciplina) 
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            p.dias[j][i] = "" #se já tem algo nesse horario
                    d.professor.remove(nome)
                    return print(disciplina + " desassociada ao aluno " + nome)
                else:
                    return print("disciplina já está associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("professor nao encontrado")
    
    def desassociar_aluno(self, nome, disciplina): 
        print("") #pular linha

        if nome in self.alunos: #se o aluno esta cadastrado
            if disciplina in self.disciplinas: #se a disciplina esta cadastrada
                a = self.alunos[nome] #salva em a o obj aluno
                d = self.disciplinas[disciplina] #salva em d o obj disciplina
                if disciplina in a.disciplinas: #checa se ele esta associado
                    a.disciplinas.remove(disciplina)
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            a.dias[j][i] = ""; #desassocia a disciplina no respectivo dia j e horario i
                    d.alunos.remove(nome)
                    return print(disciplina + " desassociada ao aluno " + nome)
                    
                else:
                    return print("disciplina não está atualmente associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("aluno nao encontrado")

    def desassociar_sala(self, nome, disciplina):
        print("") #pular linha

        if nome in self.salas: #se o sala esta cadastrada
            if disciplina in self.disciplinas: #se a disciplina esta cadastrada
                s = self.salas[nome] #salva em a o obj s
                d = self.disciplinas[disciplina] #salva em d o obj disciplina
                if disciplina in s.disciplinas:

                    s.disciplinas.remove(disciplina)
                    for j in d.dias: #percorre os dias que a disciplina é lecionada
                        for i in range(d.hora, d.hora + d.duracao): #da hora que começa, até onde termina
                            s.dias[j][i] = ""; #desassocia a disciplina no respectivo dia j e horario i
                    d.sala.remove(nome)
                    return print(disciplina + " deassociada à sala " + nome)
                else:
                    return print("disciplina não está atualmente associada")
            else: 
                return print("disciplina nao encontrada")
        else: 
            return print("aluno nao encontrado")


i = interface()

#Usei esses comandos para testes
##função alterar com alguns bugs


#lista_alunos = ['joao', 'pedro', 'carlos', 'andre', 'wallace', 'bruna', 'ana']
#for t in lista_alunos:
 #   i.criar_aluno(t)

#lista_professores = ['alberto', 'geraldo', 'pedro', 'jose']
#for t in lista_professores:
 #   i.criar_professor(t)

#lista_salas = ['10','25','110','220']
#for t in lista_salas:
  #  i.criar_sala(t,60,6,17)

#i.criar_disciplina('mat', [0,2], 10, 2, 50)
#i.criar_disciplina('port', [0,2], 8, 2, 50)
#i.criar_disciplina('bio', [1,3], 10, 2, 50)

#i.associar_professor ('alberto', 'port' )
#i.associar_professor ('alberto', 'mat' )
#i.associar_professor ('geraldo', 'bio' )

#i.associar_aluno('joao', 'port')
#i.associar_aluno('joao', 'mat')
#i.associar_aluno('joao', 'bio')

#i.associar_sala('10', 'port')
#i.associar_sala('10', 'mat')
#i.associar_sala('110', 'bio')

#i.desassociar_professor('alberto', 'port')
#i.desassociar_sala('10', 'port')
#i.desassociar_aluno('joao', 'port')

#i.excluir_disciplina ('port')
#i.excluir_professor('alberto')
#i.excluir_sala('10')
#i.excluir_aluno('joao')

i.start()


    

    
    