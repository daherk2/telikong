import telikong_cli as tcli

###################### Exemplo ########################
try:
    a = 3/0
    print a
except Exception as e:
    try:
        print tcli.chck_stackoverflow(e)
    except Exception as e:
        print tcli.chck_stackoverflow(e)