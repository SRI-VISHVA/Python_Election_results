import csv
import sqlite3
import time
import os
from csv_function import get_election_result, main_list, state_list, party_percentage
import tkinter as tk

start_time = time.time()
if os.path.exists('election_results2k19.csv'):
    with open('election_results2k19.csv', mode='r', newline='') as csv1:
        csvreader = csv.reader(csv1)
        for row in csvreader:
            try:
                if os.path.exists('election_results2k19.db'):
                    # Creating a gui for getting state name using Entry and Button
                    # top = Tk()
                    # L1 = Label(top, text='State Name')
                    # L1.pack(side=LEFT)
                    # v = StringVar
                    # E1 = Entry(top, bd=5, textvariable=v)
                    # E1.pack(side=RIGHT)
                    # s_name = v.get()
                    # B1 = Button(top, text="Find", command=party_percentage(s_name))
                    # B1.pack(side=BOTTOM)
                    # top.mainloop()
                    i = 'Y'
                    while True:
                        s_name = input('Enter the state name:\t')
                        party_percentage(s_name)
                        i = input('Do you want to repeat [Y/N] ?\t')
                        if i == 'N':
                            break
                    break
                else:
                    # Writing csv into sqlite 3 database
                    con = sqlite3.connect("election_results2k19.db")
                    cur = con.cursor()
                    cur.execute(
                        "CREATE TABLE t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name);")

                    with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
                        # csv.DictReader uses first line in file for column headings by default
                        dr = csv.DictReader(csvf)  # comma is default delimiter
                        to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'],
                                  i['Total_Votes'], i['%_of_Votes'], i['Constituency_id'], i['Constituency'],
                                  i['State_id'], i['State_name']) for i in dr]

                    cur.executemany(
                        "INSERT INTO t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
                        to_db)
                    con.commit()
                    con.close()
                    # Creating a gui for getting state name using Entry and Button
                    # top = Tk()
                    # L1 = Label(top, text='State Name')
                    # L1.pack(side=LEFT)
                    # v = StringVar
                    # E1 = Entry(top, bd=5, textvariable=v)
                    # E1.pack(side=RIGHT)
                    # s_name = v.get()
                    # B1 = Button(top, text="Find", command=party_percentage(s_name))
                    # B1.pack(side=BOTTOM)
                    # top.mainloop()
                    i = 'Y'
                    while True:
                        s_name = input('Enter the state name:\t')
                        party_percentage(s_name)
                        i = input('Do you want to repeat [Y/N] ?\t')
                        if i == 'N':
                            break
                    break
            except:
                with open('election_results2k19.csv', mode='w', newline='') as csv_file:
                    fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes', '%_of_Votes',
                                  'Constituency_id', 'Constituency', 'State_id', 'State_name']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()

                result_list = []
                for cor in main_list:
                    for s_id, c_lt in cor.items():
                        for c_id, c_name in c_lt.items():
                            result_list.append(get_election_result(int(c_id), c_name, s_id, state_list[s_id]))
                with open('election_results2k19.csv', mode='a', newline='') as csv_file:
                    for city1 in result_list:
                        for person in city1:
                            fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes', '%_of_Votes', 'Constituency_id', 'Constituency', 'State_id', 'State_Name']
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            writer.writerow({'O.S.N': person[0], 'Candidate': person[1], 'Party': person[2], 'EVM_Votes': person[3], 'Postal_Votes': person[4], 'Total_Votes': person[5], '%_of_Votes': person[6], 'Constituency_id': person[7], 'Constituency': person[8], 'State_id': person[9], 'State_Name': person[10]})

                end_time = time.time()
                writing_time = end_time - start_time
                print(writing_time)

                # Writing csv into sqlite 3 database
                con = sqlite3.connect("election_results2k19.db")
                cur = con.cursor()
                cur.execute("CREATE TABLE t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name);")

                with open('election_results2k19.csv', 'r') as csvf: # `with` statement available in 2.5+
                    # csv.DictReader uses first line in file for column headings by default
                    dr = csv.DictReader(csvf) # comma is default delimiter
                    to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'], i['Total_Votes'], i['%_of_Votes'], i['Constituency_id'], i['Constituency'], i['State_id'], i['State_name']) for i in dr]

                cur.executemany("INSERT INTO t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
                con.commit()
                con.close()
                # Creating a gui for getting state name using Entry and Button
                # top = Tk()
                # L1 = Label(top, text='State Name')
                # L1.pack(side=LEFT)
                # v = StringVar
                # E1 = Entry(top, bd=5, textvariable=v)
                # E1.pack(side=RIGHT)
                # s_name = v.get()
                # B1 = Button(top, text="Find", command=party_percentage(s_name))
                # B1.pack(side=BOTTOM)
                # top.mainloop()
                i = 'Y'
                while True:
                    s_name = input('Enter the state name:\t')
                    party_percentage(s_name)
                    i = input('Do you want to repeat [Y/N] ?\t')
                    if i == 'N':
                        break
                break
else:
    with open('election_results2k19.csv', mode='w', newline='') as csv_file:
        fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes', '%_of_Votes',
                      'Constituency_id', 'Constituency', 'State_id', 'State_name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

    result_list = []
    for cor in main_list:
        for s_id, c_lt in cor.items():
            for c_id, c_name in c_lt.items():
                result_list.append(get_election_result(int(c_id), c_name, s_id, state_list[s_id]))
    with open('election_results2k19.csv', mode='a', newline='') as csv_file:
        for city1 in result_list:
            for person in city1:
                fieldnames = ['O.S.N', 'Candidate', 'Party', 'EVM_Votes', 'Postal_Votes', 'Total_Votes', '%_of_Votes',
                              'Constituency_id', 'Constituency', 'State_id', 'State_Name']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'O.S.N': person[0], 'Candidate': person[1], 'Party': person[2], 'EVM_Votes': person[3],
                                 'Postal_Votes': person[4], 'Total_Votes': person[5], '%_of_Votes': person[6],
                                 'Constituency_id': person[7], 'Constituency': person[8], 'State_id': person[9],
                                 'State_Name': person[10]})

    end_time = time.time()
    writing_time = end_time - start_time
    print(writing_time)

    # Writing csv into sqlite 3 database
    con = sqlite3.connect("election_results2k19.db")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name);")

    with open('election_results2k19.csv', 'r') as csvf:  # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(csvf)  # comma is default delimiter
        to_db = [(i['O.S.N'], i['Candidate'], i['Party'], i['EVM_Votes'], i['Postal_Votes'], i['Total_Votes'],
                  i['%_of_Votes'], i['Constituency_id'], i['Constituency'], i['State_id'], i['State_name']) for i in dr]

    cur.executemany(
        "INSERT INTO t (O_S_N, Candidate, Party, EVM_Votes, Postal_Votes, Total_Votes, percen_of_Votes, Constituency_id, Constituency, State_id, State_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
        to_db)
    con.commit()
    con.close()
    # Creating a gui for getting state name using Entry and Button
    # top = Tk()
    # L1 = Label(top, text='State Name')
    # L1.pack(side=LEFT)
    # v = StringVar
    # E1 = Entry(top, bd=5, textvariable=v)
    # E1.pack(side=RIGHT)
    # s_name = v.get()
    # B1 = Button(top, text="Find", command=party_percentage(s_name))
    # B1.pack(side=BOTTOM)
    # top.mainloop()
    i = 'Y'
    while True:
        s_name = input('Enter the state name:\t')
        party_percentage(s_name)
        i = input('Do you want to repeat [Y/N] ?\t')
        if i == 'N':
            break
