import requests, json, string
from hashlib import sha1
from string import ascii_lowercase as alphabet

def cheker(letra, key):
    try:
        return alphabet[(alphabet.index(letra) - key) % len(alphabet)]
    except:
        return letra

def decifrar(text, key):
    out = []
    for x in text.lower():
        if x.isnumeric() or x in string.punctuation:
            out.append(x)
        else:
            out.append(cheker(x, key))
    return "".join(out)


req = requests.get("https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=TOKEN")
resposta = req.json()
decifrado = decifrar(resposta['cifrado'], resposta['numero_casas'])


resposta['decifrado'] = decifrado
resposta['resumo_criptografico'] = sha1(decifrado.encode()).hexdigest()


print(resposta)

result = requests.post("https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=TOKEN", files = {'answer': json.dumps(resposta)})

print(result.json())
