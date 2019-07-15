import requests as req
from bs4 import BeautifulSoup
import csv
import sqlite3

def get_election_result(c_id, c_name, s_id, s_name):
    resp = req.get(
        "http://results.eci.gov.in/pc/en/constituencywise/Constituencywise" + s_id + "%d.htm?ac=%d" % (c_id, c_id))
    content = resp.text
    soup = BeautifulSoup(content, features="html.parser")
    table = soup.find("table", attrs={"class": "table-party"})
    item = table.find_all("tr")[2: len(table.find_all("tr"))]
    i = 1
    city = []

    while i < len(item) - 1:
        row = []
        for data in item[i].find_all("td"):
            row.append(data.get_text())
        row.append(c_id)
        row.append(c_name)
        row.append(s_id)
        row.append(s_name)
        city.append(row)
        i = i + 1

    return city


# get_state_list()
state_list = {'U01': 'Andaman & Nicobar Islands', 'S01': 'Andhra Pradesh', 'S02': 'Arunachal Pradesh',
              'S03': 'Assam', 'S04': 'Bihar', 'U02': 'Chandigarh', 'S26': 'Chhattisgarh',
              'U03': 'Dadra & Nagar Haveli', 'U04': 'Daman & Diu', 'S05': 'Goa', 'S06': 'Gujarat',
              'S07': 'Haryana', 'S08': 'Himachal Pradesh', 'S09': 'Jammu & Kashmir', 'S27': 'Jharkhand',
              'S10': 'Karnataka', 'S11': 'Kerala', 'U06': 'Lakshadweep', 'S12': 'Madhya Pradesh',
              'S13': 'Maharashtra', 'S14': 'Manipur', 'S15': 'Meghalaya', 'S16': 'Mizoram',
              'S17': ' Nagaland', 'U05': 'NCT OF Delhi', 'S18': 'Odisha', 'U07': 'Puducherry',
              'S19': 'Punjab', 'S20': 'Rajasthan', 'S21': 'Sikkim', 'S22': 'Tamil Nadu',
              'S29': 'Telangana', 'S23': 'Tripura', 'S24': ' Uttar Pradesh', 'S28': 'Uttarakhand',
              'S25': 'West Bengal'}



# def get_state_constituency_list():
content = """<input type="hidden" id="U01" value="1,Andaman & Nicobar Islands;" />
<input type="hidden" id="S01" value="7,Amalapuram ;5,Anakapalli;19,Anantapur;1,Aruku ;15,Bapatla ;25,Chittoor ;10,Eluru ;13,Guntur;20,Hindupur;21,Kadapa;6,Kakinada;18,Kurnool;11,Machilipatnam ;17,Nandyal;14,Narasaraopet;9,Narsapuram;22,Nellore;16,Ongole ;8,Rajahmundry;24,Rajampet;2,Srikakulam;23,Tirupati ;12,Vijayawada;4,Visakhapatnam;3,Vizianagaram;" />
<input type="hidden" id="S02" value="2,ARUNACHAL EAST;1,ARUNACHAL WEST;" />
<input type="hidden" id="S03" value="3,Autonomous District;6,Barpeta;4,Dhubri;13,Dibrugarh;7,Gauhati;12,Jorhat;11,Kaliabor;1,Karimganj ;5,Kokrajhar;14,Lakhimpur;8,Mangaldoi;10,Nowgong;2,Silchar;9,Tezpur;" />
<input type="hidden" id="S04" value="9,Araria;32,Arrah;37,Aurangabad;27,Banka;24,Begusarai;26,Bhagalpur;33,Buxar;14,Darbhanga;38,Gaya (SC);17,Gopalganj (SC);21,Hajipur (SC);36,Jahanabad;40,Jamui (SC);7,Jhanjharpur;35,Karakat;11,Katihar;25,Khagaria;10,Kishanganj;13,Madhepura;6,Madhubani;19,Maharajganj;28,Munger;15,Muzaffarpur;29,Nalanda;39,Nawada;2,Paschim Champaran;31,Pataliputra;30,Patna Sahib;12,Purnia;3,Purvi Champaran;23,Samastipur (SC);20,Saran;34,Sasaram (SC);4,Sheohar;5,Sitamarhi;18,Siwan;8,Supaul;22,Ujiarpur;16,Vaishali;1,Valmiki Nagar;" />
<input type="hidden" id="U02" value="1,CHANDIGARH;" />
<input type="hidden" id="S26" value="10,BASTAR;5,BILASPUR;7,DURG;3,JANJGIR-CHAMPA;11,KANKER;4,KORBA;9,MAHASAMUND;2,RAIGARH;8,RAIPUR;6,RAJNANDGAON;1,SARGUJA;" />
<input type="hidden" id="U03" value="1,Dadra And Nagar Haveli;" />
<input type="hidden" id="U04" value="1,Daman & diu;" />
<input type="hidden" id="S05" value="1,North Goa;2,South Goa;" />
<input type="hidden" id="S06" value="7,Ahmedabad East;8,Ahmedabad West;14,Amreli;16,Anand;2,Banaskantha;23,Bardoli;22,Bharuch;15,Bhavnagar;21,Chhota Udaipur;19,Dahod;6,Gandhinagar;12,Jamnagar;13,Junagadh;1,Kachchh;17,Kheda;4,Mahesana;25,Navsari;18,Panchmahal;3,Patan;11,Porbandar;10,Rajkot;5,Sabarkantha;24,Surat;9,Surendranagar;20,Vadodara;26,Valsad;" />
<input type="hidden" id="S07" value="1,Ambala;8,Bhiwani-Mahendragarh;10,Faridabad;9,Gurgaon;4,Hisar;5,Karnal;2,Kurukshetra;7,Rohtak;3,Sirsa;6,Sonipat;" />
<input type="hidden" id="S08" value="3,Hamirpur;1,Kangra;2,Mandi;4,Shimla;" />
<input type="hidden" id="S09" value="3,Anantnag;1,Baramulla;6,Jammu;4,Ladakh;2,Srinagar;5,Udhampur;" />
<input type="hidden" id="S27" value="4,Chatra;7,Dhanbad;2,Dumka;6,Giridih;3,Godda;14,Hazaribagh;9,Jamshedpur;11,Khunti;5,Kodarma;12,Lohardaga;13,Palamau;1,Rajmahal;8,Ranchi;10,Singhbhum;" />
<input type="hidden" id="S10" value="3,Bagalkot;25,Bangalore central;24,Bangalore North;23,Bangalore Rural;26,Bangalore South;2,Belgaum;9,Bellary;7,Bidar;4,Bijapur;22,Chamarajanagar;27,Chikkballapur;1,Chikkodi;18,Chitradurga;17,Dakshina Kannada;13,Davanagere;11,Dharwad;5,Gulbarga;16,Hassan;10,Haveri;28,Kolar;8,Koppal;20,Mandya;21,Mysore;6,Raichur;14,Shimoga;19,Tumkur;15,Udupi Chikmagalur;12,Uttara Kannada;" />
<input type="hidden" id="S11" value="15,Alappuzha;9,Alathur ;19,Attingal;11,Chalakudy;12,Ernakulam;13,Idukki;2,Kannur;1,Kasaragod;18,Kollam;14,Kottayam;5,Kozhikode;6,Malappuram;16,Mavelikkara ;8,Palakkad;17,Pathanamthitta;7,Ponnani;20,Thiruvananthapuram;10,Thrissur;3,Vadakara;4,Wayanad;" />
<input type="hidden" id="U06" value="1,Lakshadweep;" />
<input type="hidden" id="S12" value="15,BALAGHAT;29,BETUL;2,BHIND;19,BHOPAL;16,CHHINDWARA;7,DAMOH;21,DEWAS;25,DHAR;4,GUNA;3,GWALIOR;17,HOSHANGABAD;26,INDORE;13,JABALPUR;8,KHAJURAHO;28,KHANDWA;27,KHARGONE;14,MANDLA;23,MANDSOUR;1,MORENA;20,RAJGARH;24,RATLAM;10,REWA;5,SAGAR;9,SATNA;12,SHAHDOL;11,SIDHI;6,TIKAMGARH;22,UJJAIN;18,VIDISHA;" />
<input type="hidden" id="S13" value="37,Ahmadnagar ;6,Akola;7,Amravati ;19,Aurangabad;35,Baramati;39,Beed;11,Bhandara - gondiya;23,Bhiwandi;5,Buldhana;13,Chandrapur;2,Dhule;20,Dindori ;12,Gadchiroli-Chimur;48,Hatkanangle;15,Hingoli ;3,Jalgaon;18,Jalna;24,Kalyan;47,Kolhapur;41,Latur ;43,Madha;33,Maval;31,Mumbai   South;26,Mumbai North;29,Mumbai North central;28,Mumbai North East;27,Mumbai North West;30,Mumbai South central;10,Nagpur ;16,Nanded;1,Nandurbar ;21,Nashik;40,Osmanabad;22,Palghar ;17,Parbhani;34,Pune;32,Raigad;9,Ramtek ;46,Ratnagiri - sindhudurg;4,Raver;44,Sangli;45,Satara;38,Shirdi;36,Shirur;42,Solapur ;25,Thane;8,Wardha;14,Yavatmal-Washim;" />
<input type="hidden" id="S14" value="1,Inner manipur;2,Outer manipur;" />
<input type="hidden" id="S15" value="1,Shillong;2,Tura ;" />
<input type="hidden" id="S16" value="1,MIZORAM;" />
<input type="hidden" id="S17" value="1,Nagaland;" />
<input type="hidden" id="U05" value="1,CHANDNI CHOWK                 ;3,EAST DELHI                    ;4,NEW DELHI                     ;2,NORTH EAST DELHI              ;5,NORTH WEST DELHI              ;7,SOUTH DELHI                   ;6,WEST DELHI                    ;" />
<input type="hidden" id="S18" value="19,Aska;6,Balasore;1,Bargarh;20,Berhampur;7,Bhadrak ;18,Bhubaneswar;10,Bolangir;14,Cuttack;9,Dhenkanal;16,Jagatsinghpur ;8,Jajpur ;11,Kalahandi;13,Kandhamal;15,Kendrapara ;4,Keonjhar ;21,Koraput ;5,Mayurbhanj ;12,Nabarangpur ;17,Puri;3,Sambalpur;2,Sundargarh ;" />
<input type="hidden" id="U07" value="1,Puducherry;" />
<input type="hidden" id="S19" value="2,Amritsar;6,Anandpur Sahib;11,Bathinda;9,Faridkot;8,Fatehgarh Sahib;10,Firozpur;1,Gurdaspur;5,Hoshiarpur;4,Jalandhar;3,Khadoor Sahib;7,Ludhiana;13,Patiala;12,Sangrur;" />
<input type="hidden" id="S20" value="13,Ajmer;8,Alwar;20,Banswara;17,Barmer;9,BHARATPUR;23,Bhilwara;2,Bikaner (SC);21,Chittorgarh;3,Churu;11,Dausa;1,Ganganagar;7,Jaipur;6,Jaipur Rural;18,Jalore;25,JHALAWAR-BARAN;4,Jhunjhunu;16,Jodhpur;10,KARAULI-DHOLPUR;24,Kota;14,Nagaur;15,Pali;22,Rajsamand;5,Sikar;12,TONK-SAWAI MADHOPUR;19,Udaipur;" />
<input type="hidden" id="S21" value="1,Sikkim;" />
<input type="hidden" id="S22" value="7,Arakkonam;12,Arani;4,Chennai central;2,Chennai North;3,Chennai South;27,Chidambaram ;20,Coimbatore;26,Cuddalore ;10,Dharmapuri;22,Dindigul;17,Erode;14,Kallakurichi;6,Kancheepuram ;39,Kanniyakumari;23,Karur;9,Krishnagiri;32,Madurai;28,Mayiladuthurai;29,Nagapattinam ;16,Namakkal;19,Nilgiris ;25,Perambalur;21,Pollachi;35,Ramanathapuram;15,Salem;31,Sivaganga;5,Sriperumbudur;37,Tenkasi ;30,Thanjavur;33,Theni ;1,Thiruvallur ;36,Thoothukkudi;24,Tiruchirappalli;38,Tirunelveli;18,Tiruppur;11,Tiruvannamalai;13,Viluppuram;34,Virudhunagar;" />
<input type="hidden" id="S29" value="1,Adilabad ;14,Bhongir ;10,CHEVELLA;9,Hyderabad;3,Karimnagar ;17,Khammam ;16,Mahabubabad  ;11,Mahbubnagar;7,Malkajgiri;6,Medak;12,Nagarkurnool;13,Nalgonda;4,Nizamabad;2,Peddapalle ;8,Secundrabad;15,Warangal;5,Zahirabad;" />
<input type="hidden" id="S23" value="2,Tripura East;1,Tripura West;" />
<input type="hidden" id="S24" value="18,Agra;44,Akbarpur;15,Aligarh;52,Allahabad;55,Ambedkar Nagar;37,Amethi;9,Amroha;24,Aonla;69,Azamgarh;23,Badaun;11,Baghpat;56,Bahraich;72,Ballia;48,Banda;67,Bansgaon;53,Barabanki;25,Bareilly;61,Basti;78,Bhadohi;4,Bijnor;14,Bulandshahr;76,Chandauli;66,Deoria;29,Dhaurahra;60,Domariyaganj;22,Etah;41,Etawah;54,Faizabad;40,Farrukhabad;49,Fatehpur;19,Fatehpur Sikri;20,Firozabad;13,Gautam Buddha Nagar;12,Ghaziabad;75,Ghazipur;70,Ghosi;59,Gonda;64,Gorakhpur;47,Hamirpur;31,Hardoi;16,Hathras;45,Jalaun;73,Jaunpur;46,Jhansi;2,Kairana;57,Kaiserganj;42,Kannauj;43,Kanpur;50,Kaushambi;28,Kheri;65,Kushi Nagar;68,Lalganj;35,Lucknow;74,Machhlishahr;63,Maharajganj;21,Mainpuri;17,Mathura;10,Meerut;79,Mirzapur;32,Misrikh;34,Mohanlalganj;6,Moradabad;3,Muzaffarnagar;5,Nagina;51,Phulpur;26,Pilibhit;39,Pratapgarh;36,Rae Bareli;7,Rampur;80,Robertsganj;1,Saharanpur;71,Salempur;8,Sambhal;62,Sant Kabir Nagar;27,Shahjahanpur;58,Shrawasti;30,Sitapur;38,Sultanpur;33,Unnao;77,Varanasi;" />
<input type="hidden" id="S28" value="3,Almora;2,Garhwal;5,Hardwar;4,Nainital-udhamsingh Nagar;1,Tehri Garhwal;" />
<input type="hidden" id="S25" value="2,Alipurduars;29,Arambagh;40,Asansol;10,Baharampur;6,Balurghat;14,Bangaon;36,Bankura;17,Barasat;39,Bardhaman Durgapur;38,Bardhaman Purba;15,Barrackpore;18,Basirhat;42,Birbhum;37,Bishnupur;41,Bolpur;1,Cooch behar;4,Darjeeling;21,Diamond harbour;16,Dum dum;32,Ghatal;28,Hooghly;25,Howrah;22,Jadavpur;3,Jalpaiguri;9,Jangipur;33,Jhargram;19,Joynagar;31,Kanthi;23,Kolkata Dakshin;24,Kolkata Uttar;12,Krishnanagar;8,Maldaha Dakshin;7,Maldaha Uttar;20,Mathurapur;34,Medinipur;11,Murshidabad;35,Purulia;5,Raiganj;13,Ranaghat;27,Srerampur;30,Tamluk;26,Uluberia;" />
"""
soup = BeautifulSoup(content, features="html.parser")
input_tag = list(soup.findAll(attrs={"type": "hidden"}))
main1_list = []

# Making a list of list: [state_id, raw string of c_id and c_name], ... ]
new_list = []
for item in input_tag:
    new_list.append([item['id'], item['value']])

last_list = []
for item in new_list:
    sno = item[0]
    value = item[1]
    c_list = []
    s_c_list = []
    val = value.split(';')

    val = list(filter(None, val))

    for item1 in val:
        value_list = []
        #     print(item1)
        c = item1.split(',')
        # print(len(c))
        cid = c[0]
        try:
            cname = c[1]
        except IndexError:
            pass
        value_list.append(cid)
        value_list.append(cname)
        c_list.append(value_list)
    s_c_list.append(sno)
    s_c_list.append(c_list)
    last_list.append(s_c_list)

main_list = []
for item in last_list:
    state = {}
    c = {}
    for item1 in item[1]:
        c[item1[0]] = item1[1]
    state[item[0]] = c
    main_list.append(state)


def party_percentage(s_name):
    party = []
    total = 0
    con = sqlite3.connect("election_results2k19.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM t")
    while True:
        row = cur.fetchone()

        if row == None:
            break
        else:
            if s_name == row[10]:
                total = total + int(row[5])
                if row[2] not in party:
                    party.append(row[2])



    party.sort()
    con.close()


    for pty in party:
                pty_total = 0
                con = sqlite3.connect("election_results2k19.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM t")
                while True:
                    row = cur.fetchone()

                    if row == None:
                        break
                    else:
                        if s_name == row[10] and pty == row[2]:
                                    pty_total = pty_total + int(row[5])
                pty_percentage = round((pty_total/float(total))*100, 2)
                print(pty + '------------>' + str(pty_percentage))
                con.close()

