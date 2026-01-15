from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()  # loads .env into environ

client = OpenAI()

def generate_voting_question(embedding_text):
    response = client.responses.create(
        model="gpt-5-nano-2025-08-07",
        input= f"Lav et ja/nej spørgsmål ud fra folketingsvalgskontekst, hvor der bliver stemt for og imod svarende til ja/nej. Returnér KUN spørgsmålet, intet andet. Spørgsmålet skal fylde mindst muligt uden at miste kontekst. \n\"{embedding_text}\""
    )
    
    return response.output_text

response = generate_voting_question("""Folketinget konstaterer, at der siden folkeafstemningen den 3. december 2015 har været afholdt tre partiledermøder og et møde mellem udenrigsministeren, justitsministeren og EU-ordførerne for at drøfte opfølgning på folkeafstemningen. Regeringen har ligeledes haft drøftelser med Kommissionen og andre interessenter i Bruxelles. Den 20. januar 2016 sendte statsministeren et brev til Kommissionens formand og formanden for Det Europæiske Råd, hvori der fra dansk side anmodes om en parallelaftale om Europol.
Folketinget bakker op om regeringens bestræbelser på at indgå en parallelaftale om Europol og støtter, at der findes en løsning, således at Danmark ikke skal forlade samarbejdet i Europol i april 2017. Om konsekvenser af kontanthjælpsloftet og 225-timersreglen.""")

print(response)