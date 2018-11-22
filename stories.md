## saudacao
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* informar_nome{"nome" : "Bruno"}
  - slot{"nome": "Bruno"}
  - utter_elogiar_nome

## saudacao2  
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* informar_nome{"nome" : "Evelyn"}
  - slot{"nome": "Evelyn"}
  - utter_elogiar_nome

## saudacao3
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* informar_nome{"nome" : "Paulo"}
  - slot{"nome": "Paulo"}
  - utter_elogiar_nome

## saudacao4
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* informar_nome{"nome" : "Roseli"}
  - slot{"nome": "Roseli"}
  - utter_elogiar_nome

## cotacao
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* perguntar_correncia{"moeda":"dólar"}
  - slot{"moeda":"dólar"}
  - action_cotar_moeda

## cotacao2
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* perguntar_correncia{"moeda":"libra"}
  - slot{"moeda":"libra"}
  - action_cotar_moeda

## cotacao3
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* perguntar_correncia{"moeda":"euro"}
  - slot{"moeda":"euro"}
  - action_cotar_moeda

## cotacao4
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* perguntar_correncia{"moeda":"real"}
  - slot{"moeda":"real"}
  - action_cotar_moeda

## conversao
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* converter_moeda{"correncia_de":"dólar","correncia_para":"real", "valor": 100}
  - slot{"correncia_de":"dólar","correncia_para":"real", "valor": 100}
  - action_converter_moeda

## conversao2
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* converter_moeda{"correncia_de":"real","correncia_para":"dolar", "valor": 200}
  - slot{"correncia_de":"real","correncia_para":"dolar", "valor": 200}
  - action_converter_moeda

## conversao3
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* converter_moeda{"correncia_de":"euro","correncia_para":"libra", "valor": 5}
  - slot{"correncia_de":"euro","correncia_para":"libra", "valor": 5}
  - action_converter_moeda

## conversao4
* saudacao
  - utter_saudacao
  - utter_perguntar_nome
* converter_moeda{"correncia_de":"libra","correncia_para":"euro", "valor": 99000}
  - slot{"correncia_de":"libra","correncia_para":"euro", "valor": 99000}
  - action_converter_moeda

## despedida
* despedida
  - utter_despedida

