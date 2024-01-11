def cari_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                     total_pasien,
                                     digit=3):
    nilai_probabilitas = []

    for jp in jumlah_pasien_penderita_penyakit:
        probabilitas = round(jp / total_pasien, digit)
        nilai_probabilitas.append(probabilitas)
        
    return nilai_probabilitas


def print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                     total_pasien,
                                     digit=3):
    nilai_probabilitas = []
    
    index = 0
    
    for jp in jumlah_pasien_penderita_penyakit:
        probabilitas = round(jp / total_pasien, digit)
        nilai_probabilitas.append(probabilitas)
        
        print('\tPasien P' + str(index+1) + ' : ' + str(jp) + '\t\t' + 
              'Probabilitas P' + str(index+1) + ' : ' + str(jp) + '/' +
              str(total_pasien) + ' = ' + str(probabilitas) + '\n')
        
        index += 1

    print('\t+---------------------+--------------------+--------------------+')
    print('\t|       PENYAKIT      |       PASIEN       |    PROBABILITAS    |')
    print('\t+---------------------+--------------------+--------------------+')

    index = 0
    
    for jp in jumlah_pasien_penderita_penyakit:
        probabilitas = round(jp / total_pasien, digit)
        nilai_probabilitas.append(probabilitas)
        print('\t|{}|{}|{}|'.format('P' + str(index+1).ljust(20),
                                      str(jp).ljust(20),
                                      str(probabilitas).ljust(20)))
        index += 1
        
    print('\t+---------------------+--------------------+--------------------+\n')


def print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit=3):
    
    print('\t+---------------------+--------------------------------+--------------------------------+--------------------------------+--------------------------------+')
    print('\t|                     |                P{}|                P{}|                P{}|                P{}|'.format(str(1).ljust(15),
                                                                                                       str(2).ljust(15),
                                                                                                        str(3).ljust(15),
                                                                                                       str(4).ljust(15)))
    print('\t|       GEJALA        +----------------+---------------+----------------+---------------+----------------+---------------+----------------+---------------+')
    print('\t|                     |     PASIEN     |  PROBABILITAS |     PASIEN     |  PROBABILITAS |     PASIEN     |  PROBABILITAS |     PASIEN     |  PROBABILITAS |')
    print('\t+---------------------+----------------+---------------+----------------+---------------+----------------+---------------+----------------+---------------+')

    indeks_gejala = 0

    nilai_probabilitas = cari_nilai_probabilitas_penyakit_per_gejala(
        gejala, jumlah_pasien_penderita_penyakit, digit)

    for i in range(0, int(len(gejala)/len(jumlah_pasien_penderita_penyakit))):
        print('\t|        G{}|       {}|       {}|       {}|       {}|       {}|       {}|       {}|       {}|'
              .format(str(i+1).ljust(12),
                      str(gejala[indeks_gejala]).ljust(9),
                      str(nilai_probabilitas[indeks_gejala]).ljust(8),
                      str(gejala[indeks_gejala+1]).ljust(9),
                      str(nilai_probabilitas[indeks_gejala+1]).ljust(8),
                      str(gejala[indeks_gejala+2]).ljust(9),
                      str(nilai_probabilitas[indeks_gejala+2]).ljust(8),
                      str(gejala[indeks_gejala+3]).ljust(9),
                      str(nilai_probabilitas[indeks_gejala+3]).ljust(8)
              )
        )
        
        indeks_gejala += 4

    print('\t+---------------------+----------------+---------------+----------------+---------------+----------------+---------------+----------------+---------------+\n')

def cari_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                jumlah_pasien_penderita_penyakit,
                                                digit=3):
    nilai_probabilitas = []
    
    indeks_gejala = 0
    ig = 0
    
    for g in gejala:
        indeks_penyakit = 0
        for jp in jumlah_pasien_penderita_penyakit:
            if indeks_gejala >= len(gejala):
                return nilai_probabilitas
            
            probabilitas = round(gejala[indeks_gejala] / jp, digit)
            nilai_probabilitas.append(probabilitas)

            indeks_gejala += 1
            indeks_penyakit += 1
            
        ig += 1
        
        
    return nilai_probabilitas


def print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                jumlah_pasien_penderita_penyakit,
                                                digit=3):
    nilai_probabilitas = []
    
    indeks_gejala = 0
    ig = 0
    
    for g in gejala:
        indeks_penyakit = 0
        for jp in jumlah_pasien_penderita_penyakit:
            if indeks_gejala >= len(gejala):
                return nilai_probabilitas
            
            probabilitas = round(gejala[indeks_gejala] / jp, digit)
            nilai_probabilitas.append(probabilitas)
            
            print('\tProbabilitas G' + str(ig+1) + ' | P' + str(indeks_penyakit+1) +
                  ' = ' + str(gejala[indeks_gejala]) + '/' + str(jp) + '\t= ' +
                  str(probabilitas))

            indeks_gejala += 1
            indeks_penyakit += 1
            
        print('\n')
            
        ig += 1
        
        
    return nilai_probabilitas

def format_nilai_probabilitas_penyakit_per_gejala(
    nilai_probabilitas_penyakit_per_gejala,
    indeks_penyakit):
    
    nilai_probabilitas = []

    for n in range(indeks_penyakit-1, len(nilai_probabilitas_penyakit_per_gejala), 4):
        nilai_probabilitas.append(nilai_probabilitas_penyakit_per_gejala[n])
    return nilai_probabilitas


def cari_nilai_probabilitas_penyakit_per_gejala_tertentu(
    nilai_probabilitas_penyakit_per_gejala, indeks_gejala):
    
    nilai_probabilitas = []
    for i in indeks_gejala:
        nilai_probabilitas.append(nilai_probabilitas_penyakit_per_gejala[i-1])
    return nilai_probabilitas


def cari_nilai_yang_dibagi(indeks_gejala,
                       indeks_penyakit,
                       gejala,
                       jumlah_pasien_penderita_penyakit,
                       total_pasien,
                       digit=3):

    unformated_npp = cari_nilai_probabilitas_penyakit_per_gejala(
        gejala, jumlah_pasien_penderita_penyakit, digit)
    
    formated = format_nilai_probabilitas_penyakit_per_gejala(
        unformated_npp, indeks_penyakit)


    npp_per_gejala_tt = cari_nilai_probabilitas_penyakit_per_gejala_tertentu(
        formated, indeks_gejala)

    hasil_perkalian_gejala = 1

    for i in npp_per_gejala_tt:
        hasil_perkalian_gejala *= i

    nilai_probabilitas_penyakit = cari_nilai_probabilitas_penyakit(
        jumlah_pasien_penderita_penyakit,
        total_pasien,
        digit)
        

    nilai_yang_dibagi = hasil_perkalian_gejala * nilai_probabilitas_penyakit[indeks_penyakit-1]
    
    return nilai_yang_dibagi
    
def print_nilai_yang_dibagi(indeks_gejala,
                       indeks_penyakit,
                       gejala,
                       jumlah_pasien_penderita_penyakit,
                       total_pasien,
                       digit=3):

    unformated_npp = cari_nilai_probabilitas_penyakit_per_gejala(
        gejala, jumlah_pasien_penderita_penyakit, digit)
    
    formated = format_nilai_probabilitas_penyakit_per_gejala(
        unformated_npp, indeks_penyakit)


    npp_per_gejala_tt = cari_nilai_probabilitas_penyakit_per_gejala_tertentu(
        formated, indeks_gejala)

    hasil_perkalian_gejala = 1

    for i in npp_per_gejala_tt:
        hasil_perkalian_gejala *= i

    nilai_probabilitas_penyakit = cari_nilai_probabilitas_penyakit(
        jumlah_pasien_penderita_penyakit,
        total_pasien,
        digit)
        

    nilai_yang_dibagi = hasil_perkalian_gejala * nilai_probabilitas_penyakit[indeks_penyakit-1]
                        
    print('\t\t(' + ' * '.join([str(np) for np in npp_per_gejala_tt]) + ' * ' +
          str(nilai_probabilitas_penyakit[indeks_penyakit-1])  + ')' + ' = ' + '(' +
          str(hasil_perkalian_gejala) + ' * ' +
          str(nilai_probabilitas_penyakit[indeks_penyakit-1])  + ')' + ' = ' +
          str(nilai_yang_dibagi))
    
    
    
    return nilai_yang_dibagi


def cari_nilai_pembagi(indeks_gejala, indeks_penyakit, gejala,
                       jumlah_pasien_penderita_penyakit,
                       total_pasien,
                       digit=3):
    
    nilai_pembagi = []
    
    for i in range(len(jumlah_pasien_penderita_penyakit)):
        nilai_pembagi.append(
            cari_nilai_yang_dibagi(indeks_gejala,
                                   i+1,
                                   gejala,
                                   jumlah_pasien_penderita_penyakit,
                                   total_pasien,
                                   digit))

    hasil_nilai_pembagi = sum(nilai_pembagi)
    
    return hasil_nilai_pembagi
                   

def print_nilai_pembagi(indeks_gejala, indeks_penyakit, gejala,
                       jumlah_pasien_penderita_penyakit,
                       total_pasien,
                       digit=3):
    
    for i in range(len(jumlah_pasien_penderita_penyakit)):
        print_nilai_yang_dibagi(indeks_gejala,
                       i+1,
                       gejala,
                       jumlah_pasien_penderita_penyakit,
                       total_pasien,
                       digit)
        if i < len(jumlah_pasien_penderita_penyakit)-1:
            print('\t\t + ')
        

def cari_nilai_probabilitas_penyakit_per_gejala_yang_dialami(
    indeks_gejala, indeks_penyakit, gejala,jumlah_pasien_penderita_penyakit,
    total_pasien, digit=3):

    nilai_yang_dibagi = cari_nilai_yang_dibagi(
                                    indeks_gejala,indeks_penyakit,
                                    gejala,
                                    jumlah_pasien_penderita_penyakit,
                                    total_pasien,
                                    digit)
    
    nilai_pembagi = cari_nilai_pembagi(
                                    indeks_gejala, indeks_penyakit,
                                    gejala,
                                    jumlah_pasien_penderita_penyakit,
                                    total_pasien,
                                    digit)

    nilai_probabilitas_penyakit_per_gejala_yang_dialami = nilai_yang_dibagi / nilai_pembagi

    return nilai_probabilitas_penyakit_per_gejala_yang_dialami


def print_nilai_probabilitas_penyakit_per_gejala_yang_dialami(
    indeks_gejala, indeks_penyakit, gejala,jumlah_pasien_penderita_penyakit,
    total_pasien, digit=3):

    nilai_yang_dibagi = cari_nilai_yang_dibagi(
                                    indeks_gejala,indeks_penyakit,
                                    gejala,
                                    jumlah_pasien_penderita_penyakit,
                                    total_pasien,
                                    digit)
    
    nilai_pembagi = cari_nilai_pembagi(
                                    indeks_gejala, indeks_penyakit,
                                    gejala,
                                    jumlah_pasien_penderita_penyakit,
                                    total_pasien,
                                    digit)

    nilai_probabilitas_penyakit_per_gejala_yang_dialami = nilai_yang_dibagi / nilai_pembagi

    print('\n')

    print('\t\t' + str(nilai_yang_dibagi))
    print('\t= --------------------------------------------------------------' +
          '--------------------------------------------------------' +
          '-------------------' )
    
    print('\t\t' + str(nilai_pembagi) + '\n\n')


    print('\t= \t' + str(nilai_probabilitas_penyakit_per_gejala_yang_dialami))



    return nilai_probabilitas_penyakit_per_gejala_yang_dialami

    
def print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit=3, persen_digit=4):

    probabilitas_penyakit = {}

    for i in range(1, len(jumlah_pasien_penderita_penyakit)+1):
        nilai_probabilitas = cari_nilai_probabilitas_penyakit_per_gejala_yang_dialami(
                                    indeks_gejala, i, gejala,
                                    jumlah_pasien_penderita_penyakit,
                                    total_pasien, digit)
        
        probabilitas_penyakit["P" + str(i)] = nilai_probabilitas

    print('\tGEJALA       : ' + ', '.join([('G' + str(g)) for g in indeks_gejala]) + '\n\n')
    print('\tKEMUNGKINAN  : ' + '\n\n')
    

    probabilitas_penyakit_terurut = dict(
        sorted(probabilitas_penyakit.items(), key=lambda x : x[1], reverse=True))

    print('\t+---------------------+--------------------+---------------------+')
    print('\t|       PENYAKIT      |   PROBABILITAS(%)  |     PROBABILITAS    |')
    print('\t+---------------------+--------------------+---------------------+')

    for key, item in probabilitas_penyakit_terurut.items():
        nilai_probabilitas_dlm_persen = round(item, persen_digit) * 100
        
        print('\t|{}|{}|{}|'.format(str(key).ljust(21),
                                    (str(nilai_probabilitas_dlm_persen) + '%') .ljust(20),
                                    str(item).ljust(21)))

    print('\t+---------------------+--------------------+---------------------+')

def print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit=3):
    
    for i in range(1, len(jumlah_pasien_penderita_penyakit)+1):

        
        print('\tProbabilitas (P{} | {})'.format(
                str(i),
                ', '.join([('G' + str(g)) for g in indeks_gejala])) + '\n\n')
    
        print_nilai_yang_dibagi(indeks_gejala, i, gejala,
                                jumlah_pasien_penderita_penyakit,
                                total_pasien, digit)
        print('\t= --------------------------------------------------------------' +
              '--------------------------------------------------------' +
              '-------------------')
        
        print_nilai_pembagi(indeks_gejala, i, gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien, digit)

        print_nilai_probabilitas_penyakit_per_gejala_yang_dialami(
            indeks_gejala, i, gejala,
            jumlah_pasien_penderita_penyakit,
            total_pasien)

        print('\n\n')
        

def test_cari_nilai_yang_dibagi():
    gejala = [
	111, 155, 90,
	105, 125, 87,
	54,  83,  54,
	47,  22,  13,
	110, 167, 85,
	38,  25,  15,
	43,  75,  45,
	20,  92,  18,
	14,  70,  13,
	15,  30,  34,
	28,  32,  28,
	30,  19,  25
    ]
    
    indeks_penyakit = 1
    indeks_gejala = [1, 2, 3, 5, 6, 7, 9, 12]
    jumlah_pasien_penderita_penyakit = [124, 173, 96]
    total_pasien = 500
    
    nilai_probabilitas = cari_nilai_probabilitas_penyakit_per_gejala_yang_dialami(
                            indeks_gejala,
                            indeks_penyakit,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit=3)
    
    print('HASIL : ' + str(nilai_probabilitas))



def demo_1():
    total_pasien = 500
    
    jumlah_pasien_penderita_penyakit = [
        124, # Jumlah Pasien Penderita P1
        173, # Jumlah Pasien Penderita P2
        96   # Jumlah Pasien Penderita P3
    ]

    gejala = [
        #P1       #P2       #P3
        
        111,      155,      90,    #G1
        105,      125,      87,    #G2 
        54,       83,       54,    #G3
        47,       22,       13,    #G4
        110,      167,      85,    #G5
        38,       25,       15,    #G6
        43,       75,       45,    #G7
        20,       92,       18,    #G8
        14,       70,       13,    #G9
        15,       30,       34,    #G10
        28,       32,       28,    #G11
        30,       19,       25     #G12
    ]
    
    indeks_gejala = [1, 2, 3, 5, 6, 7, 9, 12]

    digit = 3
    persen_digit = 4

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 4. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)

    
def demo_2():
    total_pasien = 613
    
    jumlah_pasien_penderita_penyakit = [
        227,   # Jumlah Pasien Penderita P1 (DEMAM BERDARAH)
        156,   # Jumlah Pasien Penderita P2 (MALARIA)
        119    # Jumlah Pasien Penderita P3 (CHIKUNGUYA)
    ]

    gejala = [
        #P1       #P2       #P3
        
        210,      147,      101,    #G1
        195,      128,      93,     #G2 
        202,      140,      111,    #G3
        220,      150,      115,    #G4
        156,      87,       85,     #G5
        172,      101,      81,     #G6
        42,       40,       52,     #G7
        33,       54,       28,     #G8
        56,       72,       43,     #G9
        121,      87,       39,     #G10
        128,      78,       45,     #G11
        187,      121,      65,     #G12
        39,       28,       41,     #G13
        25,       37,       52,     #G14
        192,      100,      50,     #G15
        215,      142,      107,    #G16
        57,       82,       103,    #G17
        43,       38,       21,     #G18
        37,       29,       27      #G19
    ]

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,    #G1
        3,    #G3
        5,    #G5
        6,    #G6
        8,    #G8
        10,   #G10
        11,   #G11
        12,   #G12
        15,   #G15
        16    #G16
    ]

    digit = 3
    persen_digit = 5

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)

def demo_3():
    total_pasien = 650
    
    jumlah_pasien_penderita_penyakit = [
        125,    # Jumlah Pasien Penderita P1 (INTERTRIGO)
        110,    # Jumlah Pasien Penderita P2 (MILIARIA)
        70,     # Jumlah Pasien Penderita P3 (SEBOREA)
        120     # Jumlah Pasien Penderita P4 (EKSIM)
    ]

    gejala = [
        #P1       #P2       #P3      #P4
        
    	13,       107,      8,       13,   #G1
        15,       93,       10,      14,   #G2 
        16,       104,      9,       12,   #G3
        19,       82,       7,       13,   #G4
        117,      14,       9,       111,  #G5
        110,      12,       12,      89,   #G6
        13,       13,       65,      20,   #G7
        17,       17,       12,      106,  #G8
        21,       11,       9,       99,   #G9
        18,       12,       7,       102,  #G10
        108,      13,       8,       14,   #G11
        113,      11,       7,       15,   #G12
        16,       100,      9,       12,   #G13
        15,       102,      10,      14,   #G14
        115,      15,       8,       12,   #G15
        13,       108,      10,      16,   #G16
        120,      14,       10,      115,  #G17
        13,       15,       65,      14,   #G18
        15,       13,       60,      15,   #G19
        16,       106,      9,       13,   #G20
        13,       12,       8,       117,  #G21
        15,       14,       55,      15    #G22
    ]

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,     #G1
        2,     #G2
        3,     #G3
        
        5,     #G5
        
        8,     #G8
        9,     #G9
        
        11,    #G11
        12,    #G12
        13,    #G13
        
        15,    #G15
        16,    #G16
        17,    #G17
        
        20,    #G20
        21     #G21
        
    ]

    digit = 3
    persen_digit = 5

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)

def demo_4():
    total_pasien = 650
    
    jumlah_pasien_penderita_penyakit = [
        125,    # Jumlah Pasien Penderita P1 (INTERTRIGO)
        110,    # Jumlah Pasien Penderita P2 (MILIARIA)
        70,     # Jumlah Pasien Penderita P3 (SEBOREA)
        120     # Jumlah Pasien Penderita P4 (EKSIM)
    ]

    gejala = [
        #P1       #P2       #P3      #P4
        
    	13,       107,      8,       13,   #G1
        15,       93,       10,      14,   #G2 
        16,       104,      9,       12,   #G3
        19,       82,       7,       13,   #G4
        117,      14,       9,       111,  #G5
        110,      12,       12,      89,   #G6
        13,       13,       65,      20,   #G7
        17,       17,       12,      106,  #G8
        21,       11,       9,       99,   #G9
        18,       12,       7,       102,  #G10
        108,      13,       8,       14,   #G11
        113,      11,       7,       15,   #G12
        16,       100,      9,       12,   #G13
        15,       102,      10,      14,   #G14
        115,      15,       8,       12,   #G15
        13,       108,      10,      16,   #G16
        120,      14,       10,      115,  #G17
        13,       15,       65,      14,   #G18
        15,       13,       60,      15,   #G19
        16,       106,      9,       13,   #G20
        13,       12,       8,       117,  #G21
        15,       14,       55,      15    #G22
    ]

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,     #G1
        2,     #G2
        3,     #G3
        
        5,     #G5
        
        8,     #G8
        9,     #G9
        
        11,    #G11
        12,    #G12
        13,    #G13
        
        15,    #G15
        16,    #G16
        17,    #G17
        
        20,    #G20
        21     #G21
        
    ]

    digit = 3
    persen_digit = 5

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)


def demo_5():
    total_pasien = 350

    jumlah_pasien_penderita_penyakit = [
        105,   # Jumlah Pasien Penderita P1 (MALARIA TROPICA)
        100,   # Jumlah Pasien Penderita P2 (MALARIA TERTIANA)
        85     # Jumlah Pasien Penderita P3 (MALARIA QUARTANA)
    ]

    gejala = [
        #P1       #P2       #P3
        
        15,       89,       10,     #G1
        12,       94,       79,     #G2 
        101,      12,       10,     #G3
        92,       10,       90,     #G4
        13,       15,       80,     #G5
        90,       18,       15,     #G6
        11,       78,       66,     #G7
        85,       93,       77,     #G8
        92,       14,       17,     #G9
        103,      22,       19,     #G10
        95,       91,       82,     #G11
        87,       83,       84,     #G12
    ]

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,    #G1
        2,    #G2
        3,    #G3
        6,    #G6
        7,    #G7
        8,    #G8
        9,    #G9
        11,   #G11
        12,   #G12
    ]

    digit = 3
    persen_digit = 5

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)


def demo_6():

    total_pasien = 50

    jumlah_pasien_penderita_penyakit = [
        105,   # Jumlah Pasien Penderita P1 (MALARIA TROPICA)
        100,   # Jumlah Pasien Penderita P2 (MALARIA TERTIANA)
        85     # Jumlah Pasien Penderita P3 (MALARIA QUARTANA)
    ]

    gejala = [
        #P1       #P2       #P3
        
        15,       89,       10,     #G1
        12,       94,       79,     #G2 
        101,      12,       10,     #G3
        92,       10,       90,     #G4
        13,       15,       80,     #G5
        90,       18,       15,     #G6
        11,       78,       66,     #G7
        85,       93,       77,     #G8
        92,       14,       17,     #G9
        103,      22,       19,     #G10
        95,       91,       82,     #G11
        87,       83,       84,     #G12
    ]

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,    #G1
        2,    #G2
        3,    #G3
        6,    #G6
        7,    #G7
        8,    #G8
        9,    #G9
        11,   #G11
        12,   #G12
    ]

    digit = 5
    persen_digit = 5

    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)


def demo_7():

    total_pasien = 63

    jumlah_pasien_penderita_penyakit = [
        15,   # Jumlah Pasien Penderita P1 (Gastritis)
        14,   # Jumlah Pasien Penderita P2 (Dispepsia)
        14,   # Jumlah Pasien Penderita P3 (Peptic (Tukak Lambung))
        11,   # Jumlah Pasien Penderita P4 (Gastroesophageal Reflux Disease (GERD))
         9    # Jumlah Pasien Penderita P5 (Gaster (Kanker Lambung))
    ]

    gejala = [
        #P1       #P2      #P3          #P4         #P5
        7,        3,       8,           0,           5,            #G1
        9,        0,       6,           3,           5,            #G2 
        9,        4,       0,           3,           5,            #G3
        0,        4,       8,           0,           0,            #G4
        0,        0,       10,          0,           0,            #G5
        6,        0,       1,           0,           3,            #G6
        6,        9,       3,           0,           0,            #G7
        0,        0,       0,           7,           2,            #G8
        0,        0,       0,           8,           0,            #G9
        0,        0,       0,           6,           0,            #G10
        0,        0,       0,           8,           0,            #G11
        0,        0,       2,           0,           7,            #G12
        0,        11,      0,           0,           0,            #G13
    	0,        11,      0,           0,           0,            #G14
        0,        0,       0,           5,           4,            #G15
	    5,        8,       0,           0,           3,            #G16
        14,       0,       0,           0,           0,            #G17
	    8,        4,       8,           3,           2,            #G18
        0,        0,       0,           3,           0,            #G19
	    0,        2,       0,           0,           0,            #G20
        0,        0,       8,           0,           0,            #G21
    ]

    print(gejala)

    # Gejala Yang Dirasakan Pasien / User
    
    indeks_gejala = [
        1,     #G1
        2,     #G2
        3,     #G3
        4,     #G4
        5,     #G5
        6,     #G6
        7,     #G7
        8,     #G8
        9,     #G9
        10,    #G10
        11,    #G11
        12,    #G12
        13,    #G13
        14,    #G14
        15,    #G15
        16,    #G16
        17,    #G17
        18,    #G18
        19,    #G19
        20,    #G20
        21,    #G21
    ]

    digit = 5
    persen_digit = 5


    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)


def demo_8():
    jumlah_pasien_penderita_penyakit = [
        15,   # Jumlah Pasien Penderita P1 (Gastritis)
        
        14,   # Jumlah Pasien Penderita P2 (Dispepsia)

        
        14,   # Jumlah Pasien Penderita P3 (Peptic (Tukak Lambung))

        
        11,   # Jumlah Pasien Penderita P4 (Gastroesophageal Reflux Disease (GERD))
    ]

    total_pasien = sum(jumlah_pasien_penderita_penyakit)


    gejala = [
        #P1       #P2      #P3          #P4         
    	7,	3,	8,	0,                       #G1
	    9,	0,	6,	3,                       #G2 
	    9,	4,	0,	3,                       #G3
	    0,	4,	9,	0,                       #G4
        0,	0,	12,	0,                       #G5
        6,	0,	2,	0,                       #G6
        6,	9,	4,	0,                       #G7
        0,	0,	0,	7,                       #G8
        0,	0,	0,	8,                       #G9
        0,	0,	0,	6,                       #G10
        0,	0,	0,	8,                       #G11


        0,	0,	0,	0,                       #G12
        
        0,	11,	0,	0,                       #G13
	    0,	11,	0,	0,                       #G14
        0,	0,	0,	5,                       #G15
	    5,	8,	0,	0,                       #G16
        14,	0,	0,	0,                       #G17
	    8,	4,	8,	3,                       #G18
        0,	0,	0,	3,                       #G19
	    0,	2,	0,	0,                       #G20
        0,	0,	8,	0                        #G21
    ]


    # Laplace
    for i in range(len(gejala)):
        gejala[i] += 0


    # Gastritis
    #indeks_gejala = [1,2,3,6,7,16,17,18]
    

    #Peptic (Tukak Lambung)Dispepsia (P3)
    #indeks_gejala = [1,2,4,5,6,7,18,21]

    # Dispepsia (P2)
    #indeks_gejala = [1,3,4,7,13,14,16,18,20]

    # Gastroesophageal Reflux Disease (GERD)
    indeks_gejala = [2,3,8,9,10,11,15,18,19]


    digit = 5
    persen_digit = 5


    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)

def demo_9():

    jumlah_pasien_penderita_penyakit = [
        15,   # Jumlah Pasien Penderita P1 (Gastritis)
        
        14,   # Jumlah Pasien Penderita P2 (Dispepsia)

        
        14,   # Jumlah Pasien Penderita P3 (Peptic (Tukak Lambung))

        
        11,   # Jumlah Pasien Penderita P4 (Gastroesophageal Reflux Disease (GERD))
    ]

    total_pasien = sum(jumlah_pasien_penderita_penyakit)

    gejala = [
        #P1       #P2      #P3          #P4         
	    7,	3,	8,	0,                       #G1
	    9,	0,	6,	3,                       #G2 
        9,	4,	0,	3,                       #G3
        0,	4,	9,	0,                       #G4
        0,	0,	12,	0,                       #G5
        6,	0,	2,	0,                       #G6
        6,	9,	4,	0,                       #G7
        0,	0,	0,	7,                       #G8
        0,	0,	0,	8,                       #G9
        0,	0,	0,	6,                       #G10
        0,	0,	0,	8,                       #G11


        0,	0,	8,	0,                       #G12
        
        0,	11,	0,	0,                       #G13
	    0,	11,	0,	0,                       #G14
        0,	0,	0,	5,                       #G15
	    5,	8,	0,	0,                       #G16
        14,	0,	0,	0,                       #G17
	    8,	4,	8,	3,                       #G18
        0,	0,	0,	3,                       #G19
	    0,	2,	0,	0,                       #G20
    ]


    # Laplace
    for i in range(len(gejala)):
        gejala[i] += 1


    # Gastritis
    #indeks_gejala = [1,2,3,6,7,16,17,18]
    

    #Peptic (Tukak Lambung)Dispepsia (P3)
    #indeks_gejala = [1,2,4,5,6,7,18,21]

    # Dispepsia (P2)
    #indeks_gejala = [1,3,4,7,13,14,16,18,20]

    # Gastroesophageal Reflux Disease (GERD)
    #indeks_gejala = [2,3,8,9,10,11,15,18,19]


    digit = 5
    persen_digit = 5


    indeks_gejala = [1, 2, 3, 6, 19, 20, 21]


    indeks_gejala = [4, 5, 8, 9, 10, 11, 13, 14, 15, 19, 20, 21]


    indeks_gejala = [16, 17, 21, 10, 13] # 53%

    
    indeks_gejala = [6, 3, 2, 20, 15] #64.85170164286886%

    indeks_gejala = [6, 7, 1, 8, 5]

    indeks_gejala = [7, 3, 21, 19]

    indeks_gejala = [6, 7, 2, 21]

    indeks_gejala = [18, 3, 16, 17]


    print('+----------------------------------------------------------------------------+')
    print('|                    LANGKAH 5 - PROSES TEOREMA BAYES                        |')
    print('+----------------------------------------------------------------------------+\n')
    
    print(' 1. NILAI PROBABILITAS PENYAKIT' + '\n')
    print('\tTOTAL PASIEN : ' + str(total_pasien) + '\n')

    print_nilai_probabilitas_penyakit(jumlah_pasien_penderita_penyakit,
                                      total_pasien,
                                      digit)

    print(' 2. NILAI PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_nilai_probabilitas_penyakit_per_gejala(gejala,
                                                 jumlah_pasien_penderita_penyakit,
                                                 digit)

    print(' 3. TABEL PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_table_probabilitas(gejala, jumlah_pasien_penderita_penyakit, digit)

    print(' 4. PROSES PROBABILITAS PENYAKIT KARENA GEJALA'  + '\n')

    print_proses_probabilitas_penyakit_karena_gejala(indeks_gejala,
                            gejala,
                            jumlah_pasien_penderita_penyakit,
                            total_pasien,
                            digit)

    print(' 5. KESIMPULAN'  + '\n')
    
    print_kesimpulan(indeks_gejala, gejala,
                     jumlah_pasien_penderita_penyakit,
                     total_pasien,
                     digit,
                     persen_digit)


if __name__ == '__main__':
    demo_9()