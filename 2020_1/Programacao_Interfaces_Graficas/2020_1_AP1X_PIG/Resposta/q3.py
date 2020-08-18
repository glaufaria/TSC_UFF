from operator import itemgetter
"""Representa contas e suas movimentações numa
    agência bancária."""

class Agencia(object):
    def __init__(self): # (1 ponto)
        """Cria uma nova agência sem nenhuma conta cadastrada."""
        self.agencia = []

    def cadastradas(self): # (1 ponto)
        """Retorna uma lista de todas as contas cadastradas
        nesta agência, ordenadas por número da conta."""
        contas_ordenadas = sorted(self.agencia, key=itemgetter('nconta'))
        return(contas_ordenadas)

    def saldo(self, nConta): # (0.5 ponto)
        """Retorna o saldo da conta cujo número é nConta."""
        for c in self.agencia:
            if nConta == c["nconta"]:
                return (c["saldo"])

    def limite(self, nConta): # (0.5 ponto)
        """Retorna o limite para saque a descoberto
        da conta nConta."""
        for c in self.agencia:
            if nConta == c["nconta"]:
                return (c["limite"])

    def alteraLimite(self, nConta, vLimite): # (0.5 ponto)
        """Altera o limite para saque a descoberto da conta nConta
        para vLimite, que deve ser 0 ou um npumero negativo."""
        for c in self.agencia:
            if nConta == c["nconta"]:
                c["limite"] = vLimite

    def movimenta (self, nConta, valor): # (1.5 pontos)
        """Faz um depósito ou saque.
        nConta é o número da conta e valor é a quantia a ser
        depositada (se positiva) ou a ser sacada (se negativa).
        Se a conta não existe, ela é criada, desde que o valor > 0.
        Saques só são permitidos se não ultrapassarem o limite
        de saques a descoberto da conta, definido
        por default como 0.
        Se a movimentação não for permitida, causa uma exceção
        do tipo ValueError."""

        if self.criaConta(nConta) == False:
            #executa
            #print("nao cria conta")
            if valor > 0:
                #deposito
                self.deposito(nConta,valor)
            elif valor < 0:
                #Saque
                self.saque(nConta,valor)
            else:
                print("nao é possivel realizar esta operação")
        else:
            if valor > 0:
                conta = {"nconta": nConta, "limite": 0, "extrato": [valor], "saldo": valor}
                self.agencia.append(conta)
            else:
                print("conta nao pode ser criada com mov negativa")



    def saque(self, nConta,valor):
        for c in self.agencia:
            if nConta == c["nconta"]:
                #if valor <= i["saldo"]+i["limite"]:
                if valor <= c["limite"]:
                    c["saldo"] = c["saldo"] + valor
                    c["extrato"].append(valor)
                    break
                else:
                    print("Conta sem saldo suficiente p saque")


    def deposito(self, nConta, valor):
        for c in self.agencia:
            if nConta == c["nconta"]:
                c["saldo"] = c["saldo"] + valor
                c["extrato"].append(valor)
                break

    def criaConta(self,nConta):
        criaConta =''
        for c in self.agencia:
            if nConta == c["nconta"]:
                criaConta = False
                break
        return criaConta

    def extrato(self, nConta): # (1 ponto)
        """Retorna uma lista das movimentações da conta nConta."""
        for c in self.agencia:
            if nConta == c["nconta"]:
                return(c["extrato"])

    def __str__(self):
        str=""
        for c in self.cadastradas():
            str += "conta %d, limite = %.2f" % (c["nconta"], self.limite(c["nconta"]))
            str += ",extrato = %s, saldo = %.2f\n" % (self.extrato(c["nconta"]), self.saldo(c["nconta"]))
        return str


a = Agencia()

a.movimenta(5, 100)
a.movimenta(7, 200)
a.movimenta(5, -50)
a.movimenta(2, 400)
print(a)

try:
    a.movimenta(7, -300)
except ValueError as v:
    print(v)

try:
    a.movimenta(8, -10)
except ValueError as v:
    print(v)

a.alteraLimite(7, -400)
a.movimenta(7, -300)

print(a)

'''Teste retorna:
conta 2 : limite = 0.00 , extrato = [400] , saldo = 400.00
conta 5 : limite = 0.00 , extrato = [100, -50] , saldo = 50.00
conta 7 : limite = 0.00 , extrato = [200] , saldo = 200.00
Conta sem saldo suficiente p saque
Conta nao pode ser criada com mov negativa
conta 2 : limite = 0.00 , extrato = [400] , saldo = 400.00
conta 5 : limite = 0.00 , extrato = [100, -50] , saldo = 50.00
conta 7 : limite = -400.00 , extrato = [200, -300] , saldo = -100.00'''