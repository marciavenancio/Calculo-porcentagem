print ("Consulte o valor do bônus a pagar")
tipo_assinatura = input("Por favor, digite o seu tipo de assinatura: Basic, Silver, Gold ou Platinum. ")
faturamento_anual = float(input("Por favor, digite o seu faturamento anual: "))
valor_bonus = 0

if tipo_assinatura.upper() == "BASIC":
    valor_bonus = faturamento_anual * 0.3
elif tipo_assinatura.upper() == "SILVER":
    valor_bonus = faturamento_anual * 0.2
elif tipo_assinatura.upper() == "GOLD":
    valor_bonus = faturamento_anual * 0.1
elif tipo_assinatura.upper() == "PLATINUM":
    valor_bonus = faturamento_anual * 0.05
if tipo_assinatura.upper() == "BASIC" or tipo_assinatura.upper() == "SILVER" or tipo_assinatura.upper() == "GOLD" or tipo_assinatura.upper() == "PLATINUM":
#inseri o if acima, para não exibir a mensagem do valor do bônus caso a categoria seja digitada incorretamente.
    print(
        "A sua assinatura é {} e seu faturamento anual foi R$ {:.2f}. Por isso o valor do Bônus a pagar é R$ {:.2f}.".format(
            tipo_assinatura, faturamento_anual, valor_bonus))
else:
    print("O tipo de categoria inserida é inexiste. Por favor, entrar em contato com o suporte para verificar a assinatura correta.")


