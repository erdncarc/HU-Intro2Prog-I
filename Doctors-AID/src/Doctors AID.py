try:
    ReadTXT = open("doctors_aid_inputs.txt", "r")
    WriteTXT = open("doctors_aid_outputs.txt", "w")
    ListOfPatients = []
except:
    pass

def readinginputfile():
    """Connects to the txt file and takes the inputs in order and runs them in the required function."""
    global Inputs
    for i in range(len(open("doctors_aid_inputs.txt", "r").readlines())):
        try:
            Inputs = ReadTXT.readline().rstrip("\n").split(", ")
            if Inputs == ["list"]: Function = "list"
            else:
                Function = Inputs[0].split()[0]
                Inputs[0] = Inputs[0].split()[1]
            if Function == "create": create()
            if Function == "remove": remove()
            if Function == "list": list()
            if Function == "probability": probability()
            if Function == "recommendation": recommendation()
        except:
            pass

def create():
    """Adds the patient whose information is entered to a list where all information is stored. A patient cannot be registered more than once."""
    NewPatients = [Inputs[0], Inputs[1], Inputs[2], Inputs[3], Inputs[4], Inputs[5]]
    if NewPatients not in ListOfPatients:
        ListOfPatients.append(NewPatients)
        return writingoutputfile(f"Patient {Inputs[0]} is recorded.\n")
    else: return writingoutputfile(f"Patient {Inputs[0]} cannot be recorded due to duplication.\n")

def remove():
    """Deletes the patient whose name is entered from the list. A patient not on the list cannot be deleted."""
    for i in range(len(ListOfPatients)):
        if Inputs[0] in ListOfPatients[i]:
            ListOfPatients.pop(i)
            return writingoutputfile(f"Patient {Inputs[0]} is removed.\n")
    return writingoutputfile(f"Patient {Inputs[0]} cannot be removed due to absence.\n")

def list():
    """Converts all the information in the list where the information is saved into a table."""
    writingoutputfile("Patient\tDiagnosis\tDisease\t\t\tDisease\t\tTreatment\t\tTreatment\n")
    writingoutputfile("Name\tAccuracy\tName\t\t\tIncidence\tName\t\t\tRisk\n")
    writingoutputfile("-------------------------------------------------------------------------\n")
    for Patient in ListOfPatients:
        if len(Patient[0]) < 4: writingoutputfile(Patient[0] + "\t\t")
        else: writingoutputfile(Patient[0] + "\t")
        if len(Patient[1]) < 6: writingoutputfile(str(float(Patient[1]) * 100) + "0%" + "\t\t")
        else: writingoutputfile(str(float(Patient[1]) * 100) + "%" + "\t\t")
        if len(Patient[2]) < 12: writingoutputfile(Patient[2] + "\t\t")
        else: writingoutputfile(Patient[2] + "\t")
        if len(Patient[3]) < 8: writingoutputfile(Patient[3] + "\t\t")
        else: writingoutputfile(Patient[3] + "\t")
        if len(Patient[4]) < 4: writingoutputfile(Patient[4] + "\t\t\t\t")
        elif len(Patient[4]) < 8: writingoutputfile(Patient[4] + "\t\t\t")
        elif len(Patient[4]) < 12: writingoutputfile(Patient[4] + "\t\t")
        elif len(Patient[4]) < 16: writingoutputfile(Patient[4] + "\t")
        else: writingoutputfile(Patient[4])
        if True: writingoutputfile(str(int(float(Patient[5]) * 100)) + "%" + "\n")

def probability():
    """Indicates the probability of the patient contracting the disease."""
    for i in range(len(ListOfPatients)):
        if Inputs[0] in ListOfPatients[i]:
            DiagnosisAccuracy = float(ListOfPatients[i][1])
            DiseaseIncidenceDividing = int(ListOfPatients[i][3].split("/")[0]) * DiagnosisAccuracy
            DiseaseIncidenceDivisor = int(ListOfPatients[i][3].split("/")[1])
            Process = DiseaseIncidenceDividing / ((DiseaseIncidenceDivisor - DiseaseIncidenceDividing) * (1 - DiagnosisAccuracy) + DiseaseIncidenceDividing)
            NameOfDisease = ListOfPatients[i][2].lower()
            Result = str(round(Process * 100, 2)) + "%"
            if ".0%" in Result: Result = Result[:-3] + "%"
            return writingoutputfile("Patient {} has a probability of {} of having {}.\n".format(Inputs[0], Result, NameOfDisease))
    return writingoutputfile(f"Probability for {Inputs[0]} cannot be calculated due to absence.\n")

def recommendation():
    """Indicates whether the patient should have surgery according to the probability of getting the disease."""
    for i in range(len(ListOfPatients)):
        if Inputs[0] in ListOfPatients[i]:
            DiagnosisAccuracy = float(ListOfPatients[i][1])
            DiseaseIncidenceDividing = int(ListOfPatients[i][3].split("/")[0]) * DiagnosisAccuracy
            DiseaseIncidenceDivisor = int(ListOfPatients[i][3].split("/")[1])
            Process = DiseaseIncidenceDividing / ((DiseaseIncidenceDivisor - DiseaseIncidenceDividing) * (1 - DiagnosisAccuracy) + DiseaseIncidenceDividing)
            TreatmentRisk = float(ListOfPatients[i][5])
            if TreatmentRisk <= Process: return writingoutputfile(f"System suggests {Inputs[0]} to have the treatment.\n")
            else: return writingoutputfile(f"System suggests {Inputs[0]} NOT to have the treatment.\n")
    return writingoutputfile(f"Recommendation for {Inputs[0]} cannot be calculated due to absence.\n")

def writingoutputfile(output):
    """Prints output from all processes to a new txt file."""
    WriteTXT.write(output)

try:
    readinginputfile()
    ReadTXT.close()
    WriteTXT.close()
except:
    pass

#Erdinç Arıcı
#2210356035