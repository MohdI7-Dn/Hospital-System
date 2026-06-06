#====================================Person Class===========================
from abc import ABC , abstractmethod
class Person(ABC):
    def __init__(self,name,age,ID):
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        if not isinstance(age,int):
            raise TypeError("Person age must be integers")
        if not isinstance(ID,int):
            raise TypeError("Person ID must be integers")
        if len(str(ID)) != 4:
            raise ValueError("ID must be 4 digits")
        if len(name) <= 0:
            raise ValueError("Person must have a name")
        if age <=0 or age >= 130:
            raise ValueError("Age must make sense")
        self._name = name
        self._age = age
        self._ID = ID
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if not isinstance(new_name,str):
            raise TypeError("Person name must be a string")
        if len(new_name) <= 0:
            raise ValueError("Person must have a name")
        self._name = new_name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,new_age):
        if not isinstance(new_age,int):
            raise TypeError("Person age must be integers")
        if new_age <=0 or new_age >= 130:
            raise ValueError("Person age make no sense")
        self._age = new_age
    @property
    def ID(self):
        return self._ID
    @abstractmethod
    def role(self):
        pass
    @abstractmethod
    def add_appointment(self,appointment):
        pass
    @abstractmethod
    def remove_appointment(self):
        pass
    def __eq__(self, other):
        if not isinstance(other,Person):
            return False
        return self.ID == other.ID
    def __hash__(self):
        return hash(self._ID)
#=================================Patient Class===================================
class Patient(Person):
    def __init__(self,name,age,ID,disease):
        if not isinstance(disease,str):
            raise TypeError("Disease must be a string")
        if len(disease) <=0:
            raise ValueError("Disease letters must be greater than 0")
        super().__init__(name,age,ID)
        self._disease = disease
        self._appointments = []
    @property
    def disease(self):
        return self._disease
    @disease.setter
    def disease(self,new_disease):
        if not isinstance(new_disease,str):
            raise TypeError("Disease must be a string")
        if len(new_disease) <=0:
            raise ValueError("Disease letters must be greater than 0")
        self._disease = new_disease    
    @property
    def appointments(self):
        return tuple(self._appointments)
    def __str__(self):
        return f"Name : {self._name} ({self._ID}), Age: {self._age} , Disease: {self._disease} "
    def add_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        if appointment not in self._appointments:
            self._appointments.append(appointment)   
    def role(self):
        return "Patient"
    def remove_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        self._appointments.remove(appointment) 
    def __repr__(self):
        return f"Patient({self._name},{self._ID})"
#===============================Doctor Class====================================
class Doctor(Person):
    def __init__(self,name,age,ID):
        super().__init__(name,age,ID)
        self._appointments = []
    @property
    def appointments(self):
        return tuple(self._appointments)
    def add_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        if appointment not in self._appointments:
            self._appointments.append(appointment)    
    def role(self):
        return "Doctor"
    def __str__(self):
        return f"Dr. {self._name} ({self._ID})"  
    def remove_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        self._appointments.remove(appointment)
    def __repr__(self):
        return f"Doctor({self._name},{self._ID})"
#===============================Room Class=======================================
class Room:
    def __init__(self,number,department):
        if not isinstance(number,int):
            raise TypeError("Room number must be integers")
        if not isinstance(department,str):
            raise TypeError("Room department must be a string")
        if len(str(number)) !=3:
            raise ValueError("Room number must be 3 digits")
        if len(department) <=0:
            raise ValueError("Room department letters must be greater than 0")
        self._number = number
        self._department = department
        self._appointments = []
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self,new_number):
        if not isinstance(new_number,int):
            raise TypeError("Room number must be integers")
        if len(str(new_number)) !=3:
            raise ValueError("Room number must be 3 digits")    
        self._number = new_number
    @property
    def department(self):
        return self._department
    @department.setter
    def department(self,new_department):
        if not isinstance(new_department,str):
            raise TypeError("Room department must be a string")
        if len(new_department) <=0:
            raise ValueError("Room department letters must be greater than 0")
        self._department = new_department
    @property
    def appointments(self):
        return tuple(self._appointments)
    def add_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        if appointment not in self._appointments:
            self._appointments.append(appointment)
    def __str__(self):
        return f"Room number: {self._number} , Room department: {self._department}"
    def remove_appointment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        self._appointments.remove(appointment)    
    def __eq__(self,other):
        if not isinstance(other,Room):
            return False
        return self.number == other.number
    def __hash__(self):
        return hash(self._number)
    def __repr__(self):
        return f"Room({self._number},{self._department})"
#===============================Appointment Class================================ 
from datetime import datetime
class Appointment:
    def __init__(self,patient,doctor,room,status,appointment_time):
        if not isinstance(patient,Patient):
            raise TypeError("Patient must be an object")
        if not isinstance(doctor,Doctor):
            raise TypeError("Doctor must be an object")
        if not isinstance(room,Room):
            raise TypeError("Room must be an object")
        if not isinstance(status,str):
            raise TypeError("Status must be a string")
        if len(status)  <= 0:
            raise ValueError("Status letters must be greater than 0")
        if not isinstance(appointment_time, datetime):
            raise TypeError("Appointment time must be datetime object")    
        self._patient = patient
        self._doctor = doctor
        self._room = room
        self._status = status
        self._appointment_time = appointment_time
    @property
    def appointment_time(self):
        return self._appointment_time
    @appointment_time.setter
    def appointment_time(self, new_time):
        if not isinstance(new_time, datetime):
            raise TypeError("Appointment time must be datetime object")
        self._appointment_time = new_time
    @property
    def patient(self):
        return self._patient
    @property
    def doctor(self):
        return self._doctor
    @property
    def room(self):
        return self._room
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self,new_status):
        if not isinstance(new_status,str):
            raise TypeError("Status must be a string")
        if len(new_status) <=0:
            raise ValueError("Status letters must be greater than 0")
        self._status = new_status
    def __str__(self):
        return (
            f"{self._appointment_time} | "
            f"Patient: {self._patient.name} | "
            f"Doctor: {self._doctor.name} | "
            f"Room: {self._room.number} | "
            f"Status: {self._status}"
            )
    def cancel(self):
        if self._status == "Cancelled":
            return "Already cancelled"
        self._status = "Cancelled"
    def unlink(self):
        self._patient.remove_appointment(self)
        self._doctor.remove_appointment(self)
        self._room.remove_appointment(self)    
    def __repr__(self):
        return f"Appointment({self._patient!r},{self._doctor!r},{self._room!r})"
#===================================Hospital Class==========================
class Hospital:
    def __init__(self):
        self._patients = []
        self._doctors = []
        self._rooms = []
        self._appointments = []
        self._patients_index = {}
        self._doctors_index = {}
        self._rooms_index = {}
    @property
    def patients(self):
        return tuple(self._patients)
    @property
    def doctors(self):
        return tuple(self._doctors)
    @property
    def rooms(self):
        return tuple(self._rooms)
    @property    
    def appointments(self):
        return tuple(self._appointments)
    def add_patient(self,patient):
        if not isinstance(patient,Patient):
            raise TypeError("Patient must be an object")
        if patient.ID in self._patients_index:
            return "This patient is already in system"
        self._patients.append(patient)
        self._patients_index[patient.ID] = patient
        return f"{patient.name} registed successfully"
    def add_doctor(self,doctor):
        if not isinstance(doctor,Doctor):
            raise TypeError("Doctor must be an object")
        if doctor.ID in self._doctors_index:
                return "This doctor is already in system"
        self._doctors.append(doctor)  
        self._doctors_index[doctor.ID] = doctor
        return f"{doctor.name} registed successfully"
    def add_room(self,room):
        if not isinstance(room, Room):
            raise TypeError("Room must be an object")
        if room.number in self._rooms_index:
                return "This room is already in system"
        self._rooms.append(room) 
        self._rooms_index[room.number] = room
        return f"{room.number} registed successfully"
    def find_patient_by_id(self,ID):
        if not isinstance(ID,int):
            raise TypeError("ID must be integers")
        if len(str(ID)) != 4:
            raise ValueError("ID must be 4 digits")
        return self._patients_index.get(ID)
    def find_doctor_by_id(self,ID):
        if not isinstance(ID,int):
            raise TypeError("ID must be integers")
        if len(str(ID)) != 4:
            raise ValueError("ID must be 4 digits")
        return self._doctors_index.get(ID)       
    def find_room_by_num(self,number):
        if not isinstance(number,int):
            raise TypeError("Number must be integers")
        if len(str(number)) != 3:
            raise ValueError("Room number must be 3 digits")
        return self._rooms_index.get(number)
    def remove_patient(self,ID):
        if not isinstance(ID,int):
            raise TypeError("ID must be integers")
        if len(str(ID)) != 4:
            raise ValueError("ID must be 4 digits")
        if ID not in self._patients_index:
            return "We didn't find this patient"
        patient =  self._patients_index[ID]    
        if patient not in self._patients:
            return "We didn't find this patient"
        for app in list(self._appointments):
            if app.patient.ID == ID:
                self.abort_an_appointment(app)    
        del self._patients_index[ID]
        self._patients.remove(patient)
        return "Removed"
    def remove_doctor(self,ID):
        if not isinstance(ID,int):
            raise TypeError("ID must be integers")
        if len(str(ID)) != 4:
            raise ValueError("ID must be 4 digits")
        if ID not in self._doctors_index:
            return "We didn't find this doctor"
        doctor = self._doctors_index[ID]
        if doctor not in self._doctors:
            return "We didn't find this doctor"
        for app in list(self._appointments):
            if app.doctor.ID == ID:
                self.abort_an_appointment(app)
        del self._doctors_index[ID]
        self._doctors.remove(doctor)
        return "Removed"
    def remove_room(self,num):
        if not isinstance(num,int):
            raise TypeError("Room number must be integers")
        if len(str(num)) != 3:
            raise ValueError("Room number must be 3 digits")
        if num not in self._rooms_index:
            return "We didn't find this room"
        room = self._rooms_index[num]
        if room not in self._rooms:
            return "We didn't find this room"
        for app in list(self._appointments):
            if app.room.number== num:
                self.abort_an_appointment(app)    
        del self._rooms_index[num]
        self._rooms.remove(room)
        return "Removed"
    def show_patients(self):
        for patient in self:
            print(patient)
    def show_doctors(self):
        for i in self._doctors:
            print(i)
    def show_rooms(self):
        for i in self._rooms:
            print(i)
    def show_appointments(self):
        for i in self._appointments:
            print(i)
    def abort_an_appointment(self, appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointmet must be an object")
        if appointment not in self._appointments:
            return "Not found"
        appointment.cancel()
        appointment.unlink()
        self._appointments.remove(appointment)
        return "Aborted successfully"        
    def create_an_appointment(self,doctor_ID,patient_ID,room_num,status,date):
        if not isinstance(doctor_ID,int):
            raise TypeError("Doctor_ID must be integers")
        if not isinstance(patient_ID, int):
            raise TypeError("Patient_ID must be integers")
        if not isinstance(date,datetime):
            raise TypeError("Date must be a datetime object")
        if not isinstance(room_num,int):
            raise TypeError("Room number must be integers")
        if not isinstance(status,str):
            raise TypeError("status must be a string")
        if len(status) <=0:
            raise ValueError("Status letters must be greater than 0")
        if len(str(doctor_ID)) != 4:
            raise ValueError("Doctor_ID must be 4 digits")
        if len(str(patient_ID)) != 4:
            raise ValueError("Pateint_ID must be 4 digits")
        if len(str(room_num)) != 3:
            raise ValueError("Room number must be 3 digits")
        if doctor_ID not in self._doctors_index:
            return "Doctor is not registered"
        if patient_ID not in self._patients_index:
            return "Patient is not registered"
        if room_num not in self._rooms_index:
            return "Room is not registered" 
        if date < datetime.now():
            return "Appointment cannot be in the past"    
        for appointment in self._appointments:
            if appointment.appointment_time ==date and appointment.doctor.ID == doctor_ID:
                return "Doctor already has an appointment at that time"
            if appointment.room.number == room_num and appointment.appointment_time == date:
                return "Room already reserved at that time"
            if appointment.patient.ID == patient_ID and appointment.appointment_time == date:
                return "Patient already has an appointment at that time" 
        doctor = self._doctors_index[doctor_ID]
        patient = self._patients_index[patient_ID]
        room = self._rooms_index[room_num]
        appointment = Appointment(patient,doctor,room,status,date)   
        self._appointments.append(appointment)
        patient.add_appointment(appointment)
        doctor.add_appointment(appointment)
        room.add_appointment(appointment)
        return "The reservation is done"
    def check_appoinment(self,appointment):
        if not isinstance(appointment,Appointment):
            raise TypeError("Appointment must be an object")
        if appointment not in self._appointments:
            return "We didn't find this appointment"
        if appointment.status == "Cancelled":
            return False
        return True    
    def __len__(self):
        return len(self._appointments)
    def __contains__(self,appointment):
        if not isinstance(appointment,Appointment):
            return False
        return appointment in self._appointments  
    def __iter__(self):
        return iter(self._patients)
    def __repr__(self):
        return (
            f"Hospital("
            f"patients={len(self._patients)}, "
            f"doctors={len(self._doctors)}, "
            f"rooms={len(self._rooms)}, "
            f"appointments={len(self._appointments)})"
            )    
    def __getitem__(self,patient_ID):
        if not isinstance(patient_ID,int):
            raise TypeError("ID must be integers")
        if len(str(patient_ID)) !=4:
            raise ValueError("ID must be 4 digits")
        return self._patients_index[ID]
#=======================================Test=====================================
print("\n========== START SYSTEM STRESS TEST ==========\n")
hospital = Hospital()
# =========================
# CREATE ENTITIES
# =========================
print("===== CREATE ENTITIES =====")

p1 = Patient("Ali", 25, 1001, "Flu")
p2 = Patient("Sara", 30, 1002, "Cold")
p3 = Patient("Omar", 40, 1003, "Headache")

d1 = Doctor("Ahmad", 45, 2001)
d2 = Doctor("Lina", 38, 2002)

r1 = Room(101, "Cardiology")
r2 = Room(102, "Neurology")

print(hospital.add_patient(p1))
print(hospital.add_patient(p2))
print(hospital.add_patient(p3))

print(hospital.add_doctor(d1))
print(hospital.add_doctor(d2))

print(hospital.add_room(r1))
print(hospital.add_room(r2))

print()
# =========================
# DUPLICATE TESTS
# =========================
print("===== DUPLICATE TESTS =====")
print(hospital.add_patient(p1))
print(hospital.add_doctor(d1))
print(hospital.add_room(r1))
print()
# =========================
# INVALID CREATION TESTS
# =========================
print("===== INVALID CREATION TESTS =====")
try:
    Patient(123, 25, 1004, "Flu")
except Exception as e:
    print("Patient error:", e)

try:
    Doctor("Test", "age", 2005)
except Exception as e:
    print("Doctor error:", e)

try:
    Room("101", "Cardiology")
except Exception as e:
    print("Room error:", e)

print()
# =========================
# APPOINTMENTS CREATION
# =========================
print("===== CREATE APPOINTMENTS =====")

from datetime import datetime, timedelta
t1 = datetime.now() + timedelta(days=2)
t2 = datetime.now() + timedelta(days=3)
t3 = datetime.now() + timedelta(days=4)

print(hospital.create_an_appointment(2001, 1001, 101, "Pending", t1))
print(hospital.create_an_appointment(2002, 1002, 102, "Pending", t2))
print(hospital.create_an_appointment(2001, 1003, 101, "Pending", t3))

print()

# =========================
# CONFLICT TESTS (REAL EDGE CASES)
# =========================
print("===== CONFLICT TESTS =====")

# same doctor same time
print(hospital.create_an_appointment(2001, 1002, 101, "Pending", t1))
# same room same time

print(hospital.create_an_appointment(2001, 1003, 102, "Pending", t2))

# same patient same time
print(hospital.create_an_appointment(2002, 1001, 102, "Pending", t1))

print()

# =========================
# PAST DATE TEST
# =========================
print("===== PAST DATE TEST =====")

past = datetime.now() - timedelta(days=1)
print(hospital.create_an_appointment(2001, 1001, 101, "Pending", past))

print()

# =========================
# STATE CHECK BEFORE CANCEL
# =========================
print("===== CURRENT STATE =====")

print("Appointments:")
for a in hospital.appointments:
    print(a)

print()

# =========================
# ABORT TESTS
# =========================
print("===== ABORT TESTS =====")

if hospital.appointments:
    a = hospital.appointments[0]
    print(hospital.abort_an_appointment(a))

    # abort again (should fail / edge case)
    print(hospital.abort_an_appointment(a))

print()

# =========================
# DELETE TESTS
# =========================
print("===== DELETE TESTS =====")

print(hospital.remove_patient(1003))
print(hospital.remove_doctor(2002))
print(hospital.remove_room(102))

print()

# =========================
# AFTER DELETE CHECK
# =========================
print("===== AFTER DELETE STATE =====")

print("Patients:")
for p in hospital.patients:
    print(p)

print("\nDoctors:")
for d in hospital.doctors:
    print(d)

print("\nRooms:")
for r in hospital.rooms:
    print(r)

print("\nAppointments:")
for a in hospital.appointments:
    print(a)

print()

    
print("\n===== MAGIC METHODS TEST =====")

# __repr__
print("\nHospital repr:")
print(repr(hospital))

print("\nPatient repr:")
print(repr(p1))

print("\nDoctor repr:")
print(repr(d1))

print("\nRoom repr:")
print(repr(r1))

print()

# __getitem__
print("===== GETITEM TEST =====")

print(hospital[1001])
print(hospital[1002])

try:
    print(hospital[9999])
except KeyError as e:
    print("KeyError:", e)

print()

# __iter__
print("===== ITER TEST =====")

for patient in hospital:
    print(patient)

print()

# manual iterator + next()
print("===== NEXT TEST =====")

it = iter(hospital)

try:
    while True:
        print(next(it))
except StopIteration:
    print("Iterator exhausted")

print()

# __contains__
print("===== CONTAINS TEST =====")

if hospital.appointments:
    app = hospital.appointments[0]

    print(app in hospital)
    print("hello" in hospital)
else:
    print("No appointments to test")

print()
# __len__
print("===== LEN TEST =====")

print("Appointments count:", len(hospital))

print()
# __eq__
print("===== EQUALITY TEST =====")

same_patient = Patient("Ali Clone", 99, 1001, "Test")

print(p1 == same_patient)
print(p1 == p2)

print()

# __hash__
print("===== HASH TEST =====")

patients_set = {p1, p2, p3}

print(p1 in patients_set)
print(p2 in patients_set)

clone = Patient("Clone", 50, 1001, "Test")

print(clone in patients_set)

print()

# dictionary key test
patients_dict = {
    p1: "Patient One",
    p2: "Patient Two"
}

print(patients_dict[p1])
print(patients_dict[clone])

print()

# tuple protection test
print("===== IMMUTABILITY TEST =====")

try:
    hospital.patients.append(p1)
except Exception as e:
    print(type(e).__name__, e)

try:
    p1.appointments.append("fake")
except Exception as e:
    print(type(e).__name__, e)

print()

# lookup consistency test
print("===== LOOKUP TEST =====")

print(hospital.find_patient_by_id(1001))
print(hospital.find_doctor_by_id(2001))
print(hospital.find_room_by_num(101))

print()

# remove then lookup
print("===== REMOVE + LOOKUP TEST =====")

print(hospital.remove_patient(1002))

print(hospital.find_patient_by_id(1002))

print()

# final repr after modifications
print("===== FINAL REPR =====")

print(repr(hospital))

print()

# iterate after deletion
print("===== ITERATION AFTER DELETE =====")

for patient in hospital:
    print(patient)

print()

# membership after abort
print("===== MEMBERSHIP AFTER ABORT =====")

if hospital.appointments:
    temp = hospital.appointments[0]
    print(temp in hospital)
    hospital.abort_an_appointment(temp)
    print(temp in hospital)

print()
print("\n========== END SYSTEM STRESS TEST ==========")

