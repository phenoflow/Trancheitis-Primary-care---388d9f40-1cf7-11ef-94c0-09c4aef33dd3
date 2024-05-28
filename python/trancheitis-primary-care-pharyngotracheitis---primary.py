# Chukwuma Iwundu, Clare MacRae, Eleftheria Vasileiou, 2024.

import sys, csv, re

codes = [{"code":"91647017.0","system":"snomedct"},{"code":"412577011.0","system":"snomedct"},{"code":"301087010.0","system":"snomedct"},{"code":"301074016.0","system":"snomedct"},{"code":"13306011.0","system":"snomedct"},{"code":"107009017.0","system":"snomedct"},{"code":"44623012.0","system":"snomedct"},{"code":"412576019.0","system":"snomedct"},{"code":"106996011.0","system":"snomedct"},{"code":"1.27582010000061e+16","system":"snomedct"},{"code":"301068016.0","system":"snomedct"},{"code":"989171000006116.0","system":"snomedct"},{"code":"15053015.0","system":"snomedct"},{"code":"301082016.0","system":"snomedct"},{"code":"138105010.0","system":"snomedct"},{"code":"3524071000006110.0","system":"snomedct"},{"code":"301241012.0","system":"snomedct"},{"code":"63301015.0","system":"snomedct"},{"code":"99622016.0","system":"snomedct"},{"code":"H041.00","system":"snomedct"},{"code":"H041000","system":"snomedct"},{"code":"H042000","system":"snomedct"},{"code":"H042z00","system":"snomedct"},{"code":"H042.00","system":"snomedct"},{"code":"H042.11","system":"snomedct"},{"code":"H042100","system":"snomedct"},{"code":"H16..00","system":"snomedct"},{"code":"H041100","system":"snomedct"},{"code":"H04z.00","system":"snomedct"},{"code":"H161.00","system":"snomedct"},{"code":"H31y000","system":"snomedct"},{"code":"H041z00","system":"snomedct"},{"code":"H04..00","system":"snomedct"},{"code":"H052.00","system":"snomedct"},{"code":"1.27582010000061e+16","system":"snomedct"},{"code":"106996011.0","system":"snomedct"},{"code":"412577011.0","system":"snomedct"},{"code":"91647017.0","system":"snomedct"},{"code":"138105010.0","system":"snomedct"},{"code":"301082016.0","system":"snomedct"},{"code":"301068016.0","system":"snomedct"},{"code":"412576019.0","system":"snomedct"},{"code":"301087010.0","system":"snomedct"},{"code":"107009017.0","system":"snomedct"},{"code":"63301015.0","system":"snomedct"},{"code":"3524071000006110.0","system":"snomedct"},{"code":"13306011.0","system":"snomedct"},{"code":"989171000006116.0","system":"snomedct"},{"code":"301074016.0","system":"snomedct"},{"code":"15053015.0","system":"snomedct"},{"code":"301241012.0","system":"snomedct"},{"code":"99622016.0","system":"snomedct"},{"code":"44623012.0","system":"snomedct"},{"code":"H041.00","system":"snomedct"},{"code":"H042z00","system":"snomedct"},{"code":"H042.11","system":"snomedct"},{"code":"H04..00","system":"snomedct"},{"code":"H042000","system":"snomedct"},{"code":"H16..00","system":"snomedct"},{"code":"H041100","system":"snomedct"},{"code":"H041z00","system":"snomedct"},{"code":"H161.00","system":"snomedct"},{"code":"H04z.00","system":"snomedct"},{"code":"H042.00","system":"snomedct"},{"code":"H052.00","system":"snomedct"},{"code":"H31y000","system":"snomedct"},{"code":"H042100","system":"snomedct"},{"code":"H041000","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('trancheitis-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["trancheitis-primary-care-pharyngotracheitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["trancheitis-primary-care-pharyngotracheitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["trancheitis-primary-care-pharyngotracheitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
