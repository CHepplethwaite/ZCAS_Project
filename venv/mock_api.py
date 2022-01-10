from flask import Flask, Response, stream_with_context
import time
import uuid
import random

APP = Flask(__name__)
sales_agent=['Jere Ltd','Njovu Holdings','Muyetwa Ltd','Victoria Ltd','Bupe Ltd','Kafuki Ltd']
constituency = [#Central
'Bwacha',
'Chisamba',
'Chitambo',
'Itezhi-Tezhi',
'Kabwe Central',
'Kapiri Mposhi',
'Katuba',
'Keembe',
'Lufubu',
'Mkushi North',
'Mkushi South',
'Muchinga',
'Mumbwa',
'Mwembeshi',
'Nangoma',
'Serenje',
#Copperbelt

'Bwana Mkubwa',
'Chifubu',
'Chililabombwe',
'Chimwemwe',
'Chingola',
'Kabushi',
'Kafulafuta',
'Kalulushi',
'Kamfinsa',
'Kankoyo',
'Kantanshi',
'Kwacha',
'Luanshya',
'Lufwanyama',
'Masaiti',
'Mpongwe',
'Mufulira',
'Nchanga',
'Ndola Central',
'Nkana',
'Roan',
'Wusakile',

#Eastern
'Chadiza',
'Chasefu',
'Chipangali',
'Chipata Central',
'Kapoche',
'Kasenengwa',
'Kaumbwe',
'Luangeni',
'Lumezi',
'Lundazi',
'Malambo',
'Milanzi',
'Mkaika',
'Msanzala',
'Nyimba',
'Petauke Central',
'Sinda',
'Vubwi',
#Luapula
'Bahati',
'Bangweulu',
'Chembe',
'Chienge',
'Chifunabuli',
'Chipili',
'Kawambwa',
'Mambilima',
'Mansa Central',
'Milenge',
'Mwansabombwe',
'Mwense',
'Nchelenge',
'Pambashe',
#Lusaka
'Chawama',
'Chilanga',
'Chirundu',
'Chongwe',
'Feira',
'Kabwata',
'Kafue',
'Kanyama',
'Lusaka Central',
'Mandevu',
'Matero',
'Munali',
'Rufunsa',
#Muchinga

'Chama North',
'Chama South',
'Chinsali',
'Isoka',
'Kanchibiya',
'Mafinga',
'Mfuwe',
'Mpika',
'Nakonde',
"Shiwa Ng'andu",
#Northern

'Chilubi',
'Chimbamilonga',
'Kaputa',
'Kasama',
'Lubansenshi',
'Lukashya',
'Lunte',
'Lupososhi',
'Malole',
'Mbala',
'Mporokoso',
'Mpulungu',
'Senga Hill',
#North-Western

'Chavuma',
"Ikeleng'i",
'Kabompo',
'Kasempa',
'Manyinga',
'Mufumbwe',
'Mwinilunga',
'Solwezi Central',
'Solwezi East',
'Solwezi West',
'Zambezi East',
'Zambezi West',
#Southern

'Bweengwa',
'Chikankata',
'Choma',
'Dundumwenzi',
'Gwembe',
'Kalomo Central',
'Katombola',
'Livingstone',
'Magoye',
'Mapatizya',
'Mazabuka Central',
'Mbabala',
'Monze',
'Moomba',
'Namwala',
'Pemba',
'Siavonga',
'Sinazongwe',
#Western

'Kalabo Central',
'Kaoma',
'Liuwa',
'Luampa',
'Luena',
'Lukulu East',
'Mangango',
'Mitete',
'Mongu Central',
'Mulobezi',
'Mwandi',
'Nalikwanda',
'Nalolo',
'Nkeyema',
'Senanga',
'Sesheke',
"Shang’ombo",
'Sikongo',
'Sioma',]
transaction_type=['ATM','Charge', 'Cheque','Deposit','Online','POS','Transfer','Withdrawal']
NRC_part2=['11','10']


@APP.route("/very_large_request/<int:rowcount>", methods=["GET"])
def get_large_request(rowcount):
    """returns N rows of data"""
    def f():
        """The generator of mock data"""
        for _i in range(rowcount):
            time.sleep(.2)
            txid = uuid.uuid4()
            print(txid)
            uid = uuid.uuid4()
            amount = round(random.uniform(100,1000),2) ###the range was selected to athetic purposes###
            agent = random.choice(sales_agent)
            region = random.choice(constituency)
            payment_type = random.choice(transaction_type)
            NRC1 = round(random.uniform(100000,999999))
            NRC2 = random.choice(NRC_part2)
            yield f"({agent},{region},{NRC1}/{NRC2}/1,{txid}, {uid},{payment_type}, {amount})\n"
    return Response(stream_with_context(f()))

if __name__ == "__main__":
    APP.run(debug=True)