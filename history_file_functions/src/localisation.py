from os import path, makedirs


def localize(provinces, regions, outfile, out_folder, starting_id, ending_id, sea_provinces):
    if not path.exists(out_folder):
        makedirs(out_folder)

    with open(f"{out_folder}/{outfile}", "w", encoding="ANSI") as wf:
        wf.write(";x\n")
        wf.write("#####################;x\n##### PROVINCES #####;x {"
                 "\n#####################;x\n")
        i = starting_id
        while i < ending_id + 1:
            wf.write(f"PROV{i};{provinces[str(i)]};x\n")
            i += 1

        while i >= sea_provinces[0] and i <= sea_provinces[1]:
            wf.write(f"PROV{i};{provinces[str(i)]};x\n")
            i += 1

        wf.write("###################;x }\n##### REGIONS #####;x {"
                 "\n###################;x\n")
        for i in regions:
            entered_localisation = False
            for prov_id in regions[i][1]:
                if starting_id < int(prov_id) < ending_id and not entered_localisation:
                    entered_localisation = True
                    wf.write(f"{i};{regions[i][0]};x\n")
