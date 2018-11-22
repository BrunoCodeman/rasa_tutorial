from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from forex_python.converter import CurrencyRates

moedas = { "dólar": "USD", "euro": "EUR", "real": "BRL", "libra": "GBP"}
curr = CurrencyRates()

class ConversaoAction(Action):
    def name(self): return "action_converter_moeda"

    def run(self, dispatcher, tracker, domain):
        conv = curr.get_rate('USD', 'GBP', 10) #converte 10 dólares em libras
        return [SlotSet("valor_conversao", conv)]

class CotarAction(Action):
    def name(self): return "action_cotar_moeda"

    def run(self, dispatcher, tracker, domain):
        conv = curr.get_rate('USD', 'GBP', 10) #converte 10 dólares em libras
        return [SlotSet("valor_conversao", conv)]